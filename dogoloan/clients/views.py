from django.shortcuts import render
from django.views import View
# Create your views here.\

class ClientsIndexView(View):
    template_name = 'clients/landing.html'
    def get(self, request):
        return render(request, self.template_name)
    

class CreditDataUpload(View):
    template_name = 'clients/data_upload.html'
    def get(self, request):
        return render(request, self.template_name)

    

