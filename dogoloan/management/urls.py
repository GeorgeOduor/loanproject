from django.urls import path

app_name = "management"

from .views import *

urlpatterns = [
    path("",Dashboard.as_view(),name="home"),
    path("loanapplications",LoanApplications.as_view(),name="loanapplications"),
    path("applicant_details/<str:pk>",LoanApplicatProfile.as_view(),name="applicant"),
    path("adminwallet",AdminWallet.as_view(),name="adminwallet"),
]
