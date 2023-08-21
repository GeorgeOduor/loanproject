from django.shortcuts import render
from django.views import View

# Create your views here.

class LendersHomeView(View):
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
        }
        return render(request, self.template_name,context=context)
    
class Lend(View):
    template_name = 'lenders/loanapplications.html'
    def get(self, request):
        context = {
            'user_type': 'lender',
        }
        return render(request, self.template_name,context=context)
