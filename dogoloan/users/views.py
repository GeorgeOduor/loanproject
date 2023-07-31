from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from .models import User

# Create your views here.
def ajax_view(request):
    data = {
        'name': 'George',
        'surname': 'Oduor',
        'age': 25
    }
    return JsonResponse(data)

class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')
    
class RegisterView(View):
    def get(self, request):
        return render(request, 'users/register.html')
    
    def post(self, request):
        form_data = request.POST
        password = form_data['password']
        password2 = form_data['password2']
        # chech if email exists
        if self.email_exists(form_data['email']):
            return JsonResponse({'error': 'Email already exists'})
        


def check_email_unique(request):
    if request.method == 'GET':
        email = request.GET.get('email', '')
        if User.objects.filter(email=email).exists():
            return JsonResponse({'unique': False})
        else:
            return JsonResponse({'unique': True})
        
        
        
    
class Onboarding(View):
    
    def get(self,request):
        return render(request, 'users/onboarding.html')