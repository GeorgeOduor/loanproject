from django.shortcuts import render
from django.views import View
from time import sleep
# Create your views here.
from .models import LoanProduct,LenderProfile

class LendersDashboard(View):
    template_name = 'lenders/dashboard.html'
    def get(self, request):
        context = {
            'user_type': 'lender',
        }
        return render(request, self.template_name,context=context)

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

def lender_application(request,category):
    if request.method == 'GET':
        if category == 'products':
            # fetch products
            lender_profile = LenderProfile.objects.get(user = request.user)
            products = LoanProduct.objects.filter(lender = lender_profile)
            context = {
                'products': products
            }
            return render(request, 'includes/products.html',context=context)
        if category == 'agents':
            return render(request,'includes/agents.html')
        
    
class LenderProfileView(View):
    template_name = 'lenders/lenderprofile.html'
    def get(self, request):
        context = {
            'user_type': 'lender',
        }
        return render(request, self.template_name,context=context)

class Lend(View):
    template_name = 'lenders/loanapplications.html'
    def get(self, request):
        context = {
            'user_type': 'lender',
        }
        return render(request, self.template_name,context=context)
