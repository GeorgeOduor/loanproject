from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.
from users.models import Profile
from .models import BorrowerProfile
from lenders.models import LoanProduct,LenderProfile,LoanApplications,LoansCounter,Transaction
from scripts.automations import get_loan_balance
from django.contrib import messages


@method_decorator(login_required, name='dispatch')
class BorrowerLandingView(View):
    def get(self,request):
        balances = get_loan_balance(request.user.id,Transaction)
        # print(balances,"----------------------")

        context = {
            'user_type': 'borrower',
        }
        if balances:
            context['loan_balance'] = f"{balances.balance:,.2f}"
            context['balances']     = balances

        return render(request, 'borrowers/landing.html',context)
    
    def post(self,request):
        form_data = request.POST
        mobile_no = form_data.get('mobile_no')
        # pay loan
        current_loan_balance = get_loan_balance(request.user.id,Transaction)
        try:
            _,ret_message = Transaction.objects.create_repayment_transaction(
                borrower             = request.user,
                lender               = LenderProfile.objects.get(id = form_data.get('lender')),
                product              = LoanProduct.objects.get(id = form_data.get('product')),
                amount               = float(form_data.get('amount')),
                current_loan_balance = current_loan_balance.balance,
                mpesa_trx_id         = form_data.get('mpesa_trx_id')
            )
            messages.success(request,ret_message)
            return redirect('borrow:borrower_landing')
        except Exception as e:
            message = f"Loan payment failed: {e}"
            messages.error(request,message)
            return redirect('borrow:borrower_landing')

@method_decorator(login_required, name='dispatch')
class BorrowerProfileView(View):
    profile  = Profile.objects
    borrower = BorrowerProfile.objects
    def get(self,request):
        profile = self.profile.get(user=request.user)
        borrower = self.borrower.get(user=request.user)
        context = {
            'user_type': 'borrower',
            'first_name': profile.first_name,
            'last_name' : profile.last_name,
            'mobile_no' : profile.user.msisdn,
            'email'     : profile.email_address,
            # physical address
            'country'   : borrower.country,
            'county'    : borrower.county,
            'zip_code'  : borrower.zip_code,
            # demographics
            'marital_status' : borrower.marital_status,
            'education': borrower.education,
            'employment_status': borrower.employment_status,
            'employment_sector': borrower.employment_sector,
            'income_range': borrower.income_range,
            # more contact
            'referer_mobile_number': borrower.referer_mobile_number,
            'alternative_mobile_number': borrower.alternative_mobile_number
            
        }
        
        return render(request, 'lenders/profile.html',context=context)
    
    def post(self,request):
        form_data = request.POST
        form_files = request.FILES

        first_name = form_data.get('first_name')
        last_name  = form_data.get('last_name')
        email      = form_data.get('email')
        mobile_no  = form_data.get('main_mobile_no')
        # demographics
        marital_status = form_data.get('marital_status')
        education = form_data.get('education')
        employment_status = form_data.get('employment_status')
        employment_sector = form_data.get('employment_sector')
        income_range = form_data.get('income_range')
        # physical address
        country = form_data.get('country')
        county = form_data.get('county')
        zip_code = form_data.get('zip_code')
        # more contact
        referer_mobile_number = form_data.get('referer_mobile_number')
        alternative_mobile_number = form_data.get('alternative_mobile_number')

        try:
            # update profile
            Profile.objects.filter(user=request.user).update(
                first_name=first_name,
                last_name=last_name,
                email_address=email,
            )
            # update borrower
            BorrowerProfile.objects.filter(user=request.user).update(
                marital_status=marital_status,
                education=education,
                employment_status=employment_status,
                employment_sector=employment_sector,
                income_range=income_range,
                county=county,
                zip_code=zip_code,
                referer_mobile_number=referer_mobile_number,
                alternative_mobile_number=alternative_mobile_number
            )
            return JsonResponse({'message': 'Data updated successfully'})
        except:
            return JsonResponse({'error': 'Something went wrong,please try again'})
        
@method_decorator(login_required, name='dispatch')
class AvailableLoansView(View):
    
    # lenders = LenderProfile
    def get(self,request):
        loanproducts = LoanProduct.objects.select_related('lender').filter(status = "Active")
        balances = get_loan_balance(request.user.id,Transaction)
        if balances:
            balances = balances.balance > 0
        else:
            balances = False
        try:
            context = {
                'user_type': 'borrower',
                'lenders':loanproducts,
                'products':len(loanproducts.values()),
                'balances': balances

            }
            return render(request, 'borrowers/available_lenders.html',context=context)
        except Exception as e:
            raise e
            return JsonResponse({'error': f'Something went wrong,please try again:{e}'})
        
    def post(self,request):
        loan_request_data = request.POST
        lender_id         = loan_request_data.get('lender_id')
        product_id        = loan_request_data.get('product_id')
        principle         = loan_request_data.get('loan_amount')
        interest_rate     = loan_request_data.get('interest_rate')
        facilitation_fees = loan_request_data.get('facilitation_fees')
        total_loan_amount = loan_request_data.get('total_loan_amount')
        try:
            # check if user has applied for the same loan and waiting approval
            existing_application = LoanApplications.objects.filter(
                borrower           = request.user,
                loan_product_id    = product_id,
                application_status = "Pending"
                ).exists()
            if existing_application:
                messages.error(request, 'You have already applied for this loan and are waiting for approval')
                return redirect('borrow:borrower_landing')
            else:
                lender = LenderProfile.objects.get(id = lender_id)
                LoanApplications.objects.create(
                    lender             = lender,
                    loan_product       = LoanProduct.objects.get(id = product_id),
                    borrower           = request.user,
                    principle          = principle,
                    interest           = interest_rate,
                    fees               = facilitation_fees,
                    total              = total_loan_amount,
                    application_status = "Pending",
                    has_previous_loan  = False
                    )
                # update requests counter
                counter = LoansCounter.objects.filter(lender = lender)
                if counter.exists():
                    total_requests = counter[0].applied_loans + 1
                    counter.update(applied_loans = total_requests)
                else:
                    LoansCounter.objects.create(
                        lender = lender,
                        applied_loans = 1
                    )
                messages.success(request, 'Loan application submitted successfully')
                return redirect('borrow:borrower_landing')
        except Exception as e:
            messages.error(request, f'Something went wrong,please try again. {e}')
            return redirect('borrow:borrower_landing')
        return JsonResponse({'message': loan_request_data})

@login_required
def loan_balance(request):
    # borrower identification
    borrower_id = request.user.id
    # get loan balance
    loan_balance = Transaction.objects.filter(borrower=borrower_id).order_by('-transaction_date')

    if loan_balance.exists():
        loan_balance = loan_balance[0].balance
    else:
        loan_balance = 0
    
    return JsonResponse({"loan_balance": loan_balance})
