from django.urls import path
from .views import *
app_name = "borrow"

urlpatterns = [
    path('',BorrowerLandingView.as_view(),name="borrower_landing"),
    path('loans',AvailableLoansView.as_view(),name="available_loans"),
    path('profile',BorrowerProfileView.as_view(),name="borrower_profile"),
    path('loan_balance',loan_balance,name="loan_balance"),
]
