from django.shortcuts import render
from django.urls import path
from .views import *
# Create your views here.
app_name = 'lenders'

urlpatterns = [
    path("", Lend.as_view(), name="lend"),
    path("stats/", LendersDashboard.as_view(), name="lender_dashboard"),
    path("mywallet/", LendersWallet.as_view(), name="lender_wallet"),
    path("settings", LenderSettings.as_view(), name="lender_settings"),
    path("loanapplications/<str:category>", lender_application, name="lender_application"),
    path("profile", LenderProfileView.as_view(), name="profile"),
    path('credit_information/<int:pk>/<int:application_id>', CreditDetails.as_view(), name="credit_information"),
    path('loan_approval/<int:application_id>', loan_approval, name="approve_loan"),
]



