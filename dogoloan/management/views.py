from django.shortcuts import render
from django.views import View
# Create your views here.

class Dashboard(View):
    
    def get(self, request):
        return render(request, 'management/dashboard.html')
    
class LoanApplications(View):

    def get(self,request):
        return render(request,"management/loanapplications.html")
    
class LoanApplicatProfile(View):

    def get(self,request,pk):
        return render(request,'management/applicantdetails.html')
    
class AdminWallet(View):

    def get(self,request):
        return render(request,'management/adminwallet.html')