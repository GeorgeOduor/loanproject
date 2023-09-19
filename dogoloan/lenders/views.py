from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views import View
from time import sleep
from django.contrib import messages
# Create your views here.
from .models import LoanProduct,LenderProfile
from users.models import Profile

class LendersDashboard(View):
    template_name = 'lenders/dashboard.html'
    def get(self, request):
        context = {
            'user_type': 'lender',
            }
        return render(request, self.template_name,context=context)

class LenderProfileView(View):
    template_name = 'lenders/profile.html'
    profiles = Profile.objects
    lenders = LenderProfile.objects
    
    def get(self, request):
        profile = self.profiles.get(user=request.user)
        lender = self.lenders.get(user=request.user)
        
        context = {
            'user_type' : 'lender',
            'first_name': profile.first_name,
            'last_name' : profile.last_name,
            'mobile_no' : profile.user.msisdn,
            'email'     : profile.email_address,
            'paybillno' : lender.paybillno,
            'brand'     : lender.brand,
            'zip_code'  : lender.zip_code,
            'county'    : lender.county,
            'industry'  : lender.industry,
            'town'      : profile.town
        }
        
        return render(request, self.template_name,context=context)
    
    def post(self,request):
        context = {
            'user_type': 'lender',
        }
        form_data           = request.POST
        # profile information
        userProfile = Profile.objects.get(user = request.user)
        userProfile.first_name    = form_data['first_name']
        userProfile.last_name     = form_data['last_name']
        userProfile.email_address = form_data['email']
        userProfile.town          = form_data['town']
        userProfile.save()
        # Lender profile information
        if not self.lenders.filter(user = request.user).exists():
            LenderProfile.objects.create(user = request.user)
        lender_profile = self.lenders.get(user = request.user)
        lender_profile.lending_mobile_no = form_data['mobile_number']
        lender_profile.paybillno         = form_data['paybillno']
        lender_profile.brand             = form_data['brand']
        lender_profile.zip_code          = form_data['zip_code']
        lender_profile.county            = form_data['county']
        lender_profile.country           = "Kenya"
        lender_profile.industry          = form_data['industry']
        lender_profile.save()
        return JsonResponse({'message': "Your profile has been updated successfully,Happy Lending!"})

class LendersWallet(View):
    template_name = 'lenders/adminwallet.html'
    
    def get(self, request):
        context = {
            'user_type': 'lender',
        }
        return render(request, self.template_name,context=context)

class LoanApplications(View):
    template_name = 'lenders/loanapplications.html'
    def get(self, request):
        context = {
            'user_type': 'lender',
        }
        return render(request, self.template_name,context=context)

class LenderSettings(View):
    template_name = 'lenders/settings.html'

    def get(self, request):
        context = {
            'user_type': 'lender',
            # 'category': category
        }
        return render(request, self.template_name,context=context)
    
    def post(self, request):
        context = {
            'user_type': 'lender',
            # 'category': category
        }
        form_data           = request.POST
        product_id          = form_data['product_id']
        form_action        = form_data['form_action']
        # add new product
        if form_action == 'add_new':
            # add new product
            try:
                LoanProduct.objects.create(
                    lender              = LenderProfile.objects.get(user=request.user),
                    name                = form_data['product_name'],
                    interest_rate       = form_data['interest_rate'],
                    repayment_term      = form_data['repayment_term'],
                    penalties           = form_data['penalties'],
                    min_loan_amount     = form_data['min_loan_amount'],
                    max_loan_amount     = form_data['max_loan_amount'],
                    product_description = form_data['productDescription'],
                    status              = form_data['status'],
                )

                success_message = f"Product {form_data['product_name']} added successfully"
                return JsonResponse({'message': success_message})
            except Exception as e:
                print(e)
                return JsonResponse({'errors': str(e)})
        elif form_action == 'update':
            # update product
            try:
                # fetch product
                product                     = LoanProduct.objects.get(id=product_id)
                product.name                = form_data['product_name']
                product.interest_rate       = form_data['interest_rate']
                product.repayment_term      = form_data['repayment_term']
                product.penalties           = form_data['penalties']
                product.min_loan_amount     = form_data['min_loan_amount']
                product.max_loan_amount     = form_data['max_loan_amount']
                product.product_description = form_data['productDescription']
                product.status              = form_data['status']
                product.save()
                success_message = f"Product {form_data['product_name']} updated successfully"
                return JsonResponse({'message': success_message})
            except Exception as e:
                print(e)
                return JsonResponse({'errors': str(e)})
        # delete product
        elif form_action == 'delete':
            # delete product
            try:
                product         = LoanProduct.objects.get(id=product_id)
                # check if product has applications
                product.delete()
                messages.success(request, 'Product deleted successfully')
                return redirect('lenders:lender_settings')
            except Exception as e:
                messages.error(request, f'Product could not be deleted due to {e}')
                return render(request, self.template_name,context=context)
        # deactivate/archive product
        elif form_action == 'archive':
            try:
                product         = LoanProduct.objects.get(id=product_id)
                product.status  = 'Inactive'
                product.save()
                messages.success(request, 'Product archived successfully')
                return redirect('lenders:lender_settings')
            except Exception as e:
                messages.error(request, f'Product could not be archived due to {e}')
                return render(request, self.template_name,context=context)
        else:
            print(form_data)


        # return render(request, self.template_name,context=context)

def lender_application(request,category):
    if request.method == 'GET':
        if category == 'products':
            # fetch products
            try:
                lender_profile = LenderProfile.objects.get(user = request.user)
                products = LoanProduct.objects.filter(lender = lender_profile)
                context = {
                    'products': products
                }
                return render(request, 'includes/products.html',context=context)
            except Exception as e:
                return render(request, 'includes/products.html')
        if category == 'agents':
            return render(request,'includes/agents.html')
        
class Lend(View):
    template_name = 'lenders/loanapplications.html'
    def get(self, request):
        context = {
            'user_type': 'lender',
        }
        # check if user's lender profile is set
        lender_profile = LenderProfile.objects.filter(user = request.user)

        if lender_profile.exists():
            # check if profile fields are complete
            return render(request, self.template_name,context=context)
        else:
            return redirect('lenders:profile')
        
    def post(self, request):
        context = {
            'user_type': 'lender',
        }
        form_data           = request.POST
        
        
