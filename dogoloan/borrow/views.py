from django.shortcuts import render
from django.views import View
# Create your views here.
from users.models import Profile
from .models import BorrowerProfile

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
            
        }
        
        return render(request, 'lenders/profile.html',context=context)

class AvailableLenders(View):

    def get(request):
        context = {
            'user_type': 'borrower',
        }
        return render(request, 'borrowers/available_lenders.html',context=context)
