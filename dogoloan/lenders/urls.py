from django.shortcuts import render
from django.urls import path
from .views import LendersHomeView,Lend,LendersWallet,LenderSettings
# Create your views here.
app_name = 'lenders'

urlpatterns = [
    path("", Lend.as_view(), name="lend"),
    path("stats/", LendersHomeView.as_view(), name="lender_dashboard"),
    path("mywallet/", LendersWallet.as_view(), name="lender_wallet"),
    path("settings/", LenderSettings.as_view(), name="lender_settings"),

]



