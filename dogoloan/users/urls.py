from django.urls import path

from .views import *

app_name = "users"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("onboarding", Onboarding.as_view(), name="onboarding"),
    # ajax_views
    path("ajax_view/", ajax_view, name="ajax_view"),
]
