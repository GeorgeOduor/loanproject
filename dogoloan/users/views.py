from django.shortcuts import render,redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.auth import authenticate, login

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
        return render(request, 'users/register.html')
    
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
            profileinfo.nationa_id    = data['nationalid']
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
    

# class UserProfile(View):
#     def get(self,request):
#         if not request.user.is_authenticated:
#             return redirect('users:login')
#         return render(request, 'users/profile.html')