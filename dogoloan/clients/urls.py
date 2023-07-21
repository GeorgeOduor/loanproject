from django.urls import path
from .views import *

app_name = "clients"

urlpatterns = [
    path("", ClientsIndexView.as_view(),name="home"),
]