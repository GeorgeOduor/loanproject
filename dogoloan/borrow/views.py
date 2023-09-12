from django.shortcuts import render
from django.views import View
# Create your views here.


class BorrowerProfile(View):
    def get(self,request):
        context = {
            'user_type': 'borrower',
        }
        return render(request, 'lenders/profile.html',context=context)

class AvailableLenders(View):

    def get(request):
        context = {
            'user_type': 'borrower',
        }
        return render(request, 'borrowers/available_lenders.html',context=context)
