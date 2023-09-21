from django.urls import path
from .views import *
app_name = "borrow"

urlpatterns = [
    path('profile',BorrowerProfileView.as_view(),name="borrower_profile"),
]
