from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
# Create your views here.
from users.models import Profile
from .models import BorrowerProfile
from lenders.models import LoanProduct,LenderProfile

class BorrowerLandingView(View):
    def get(self,request):
        context = {
            'user_type': 'borrower',
        }
        return render(request, 'borrowers/landing.html',context)

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
        


class AvailableLoansView(View):
    loanproducts = LoanProduct.objects.select_related('lender')#.filter(status = "Active")
    # lenders = LenderProfile
    def get(self,request):
        
        try:
            context = {
                'user_type': 'borrower',
                'lenders':self.loanproducts

            }
            print(self.loanproducts.values())
            
            return render(request, 'borrowers/available_lenders.html',context=context)
        except Exception as e:
            raise e
            return JsonResponse({'error': f'Something went wrong,please try again:{e}'})
