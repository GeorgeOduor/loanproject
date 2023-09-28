from django.shortcuts import render,redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.auth import authenticate, login,logout
from borrow.models import BorrowerProfile
from lenders.models import LenderProfile


from .models import User,Profile

# Create your views here.
def ajax_view(request):
    data = {
        'name': 'George',
        'surname': 'Oduor',
        'age': 25
    }
    return JsonResponse(data)

class LoginView(View):
    """
    A Django view that handles the GET request for the login page.
    """

    def get(self, request):
        # check if user is authenticated
        if request.user.is_authenticated:
            return redirect('users:onboarding')
        return render(request, 'users/login.html')
    
    def post(self,request):
        data = request.POST
        password = data['password']
        msisdn   = f"254{data['mobile'][-9:]}"
        # authenticate
        user = authenticate(request, msisdn=msisdn, password=password)
        
        if user:
            login(request, user)
            return JsonResponse({'message': 'Login Successfull'})
        else:
            return JsonResponse({'error': 'Invalid Credentials'})
    
class RegisterView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'users/register.html')
        return render(request, 'users/onboarding.html')
    
    def post(self, request):
        data = request.POST
        error_messages = []  # Initialize a list to store error messages
        # Check if passwords match
        if data['password'] != data['password2']:
            error_messages.append('Passwords do not match')
        # Check if email exists
        if self.email_exists(data['email_address']):
            error_messages.append('Email already exists')
        # Check if mobile exists
        if self.mobile_exists(data['msisdn']):
            error_messages.append('Mobile number already exists')

        # If there are any error messages, return them
        if error_messages:
            print(error_messages)
            return JsonResponse({'errors': error_messages})
        
        try:
            # perform registration
            user = User.objects.create_user(
                msisdn   = data['msisdn'],
                password = data['password'],
                )
            profileinfo               = Profile.objects.get(user=user)
            profileinfo.first_name    = data['fname']
            profileinfo.last_name     = data['lname']
            profileinfo.gender        = data['gender']
            profileinfo.date_of_birth = data['dob']
            profileinfo.email_address = data['email_address']
            profileinfo.town          = data['town']
            profileinfo.national_id    = data['nationalid']
            profileinfo.social_reach  = data['social_reach']
            profileinfo.save()
            return JsonResponse({'message': 'Data submitted successfully'})
        except Exception as e:
            print(e)
            return JsonResponse({'errors': str(e)})

        
    def clean_gender(self, gender):
        """
        Clean Gender column
        """
        if gender in ['Male', 'Female']:
            return True
        else:
            return False

    
    def email_exists(self, email):
        """
        Check if the email already exists in the User objects.
        """
        try:
            Profile.objects.get(email_address=email)
            return True
        except Profile.DoesNotExist:
            return False
    
    def mobile_exists(self, msisdn):
        """
        Check if the mobile number already exists in the User objects.
        """
        try:
            User.objects.get(msisdn=f"254{msisdn[-9:]}")
            return True
        except User.DoesNotExist:
            return False
    
class Onboarding(View):
    def get(self,request):
        if not request.user.is_authenticated:
            return redirect('users:login')
        return render(request, 'users/onboarding.html')
# logout view

def logout_view(request):
    logout(request)
    return redirect("users:login")

class AccountsVerification(View):

    def get(self,request,user_action):

        if not request.user.is_authenticated:
            return redirect('users:login')
        
        # check if user is active
        if user_action == "lend":
            lender_profile = LenderProfile.objects.get(user = request.user)
            if lender_profile.status == "Active":
                return redirect('/lend/')
        elif user_action == "borrow":
            borrower_profile = BorrowerProfile.objects.get(user = request.user)
            if  borrower_profile.status == "Active":
                return redirect('/borrow/')
        else:
            return redirect('users:onboarding')
        
        # print(user_action,"----------------")
        context = {
            'user_action': user_action,
            'first_name': Profile.objects.get(user=request.user).first_name
        }
        return render(request, 'users/accounts_verification.html',context)
    
    def post(self,request,user_action):
        
        files_data = request.FILES
        if user_action == "lend":
            return self.update_lender_info(request)
        elif user_action == "borrow":
            return self.update_borrower_info(request)
   
        
        # verify uploaded id
        if self.verify_national_id(request):
            return redirect('users:onboarding')


        return redirect('users:onboarding')
    
    def update_borrower_info(self,request):
        form_data = request.POST
        # check if borrower profile exists and create if missing
        if not BorrowerProfile.objects.filter(user=request.user).exists():
            BorrowerProfile.objects.create(user=request.user)
        # form data
        employment = form_data['employment']
        if employment in ['employed', 'self-employed']:
            employment_sector = form_data['employment_sector']
        else:
            employment_sector = ""
        education = form_data['education']
        marital_status = form_data['marital_status']
        income_range = form_data['income_range']
        county = form_data['county']
        altenative_mobile_number = form_data['altenative_mobile_number']
        if "referer_mobile_number" in form_data:
            referer_mobile_number = form_data['referer_mobile_number']
        # check errors
        if any([county == "", altenative_mobile_number == "",employment == "Employment Status:",\
               employment_sector == "Specify sector:",education == "Highest Level of Education:",\
               marital_status == "Marital Status:",income_range == "Income Range(Ksh) per month:"]): 
            return JsonResponse({'error': 'Please fill all the fields'})
           # verify id
        # update borrowers table and set status to active
        BorrowerProfile.objects.filter(user=request.user).update(
            employment_status = employment,
            employment_sector = employment_sector,
            education = education,
            marital_status = marital_status,
            income_range = income_range,
            county = county,
            alternative_mobile_number = altenative_mobile_number,
            referer_mobile_number = referer_mobile_number,
            status = "Inactive"
        )

        return JsonResponse({'message': 'Data submitted successfully'})
    

    def update_lender_info(self,request):
        form_data = request.POST
        # check if lender profile exists and create if missing
        if not LenderProfile.objects.filter(user=request.user).exists():
            LenderProfile.objects.create(user=request.user)
        lending_as = form_data['lending_as']
        industry   = form_data['industry']
        brand      = form_data['brand']
        county     = form_data['county']
        town       = form_data['town']
        zip_code   = form_data['zip_code']
        # check errors
        if industry == "Prefered Industry" or lending_as == "I want to lend as:" or county == "":
            return JsonResponse({'error': 'Please fill all the fields'})
        # update profiles table
        Profile.objects.filter(user=request.user).update(
            town=town,
        )
        # verify id 
            # update lenders table and set status to active 
        LenderProfile.objects.filter(user=request.user).update(
            lending_as = lending_as,industry= industry,
            brand= brand,county  = county,zip_code= zip_code,
            status  = "Active")

        return JsonResponse({'message': 'Data submitted successfully'})
    
    def verify_national_id(self,request):
        files = request.FILES
        # logic to scrap text from image
        return True
            