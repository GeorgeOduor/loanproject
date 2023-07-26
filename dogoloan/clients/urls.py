from django.urls import path
from .views import *

app_name = "clients"

urlpatterns = [
    path("", ClientsIndexView.as_view(),name="home"),
    path("mycredit_data",CreditDataUpload.as_view(),name="credit_data")
]