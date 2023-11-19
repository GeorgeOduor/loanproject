from django.urls import path

from .views import *

app_name = "users"

urlpatterns = [
    # path("", UserProfile.as_view(), name="profile"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("onboarding/", Onboarding.as_view(), name="onboarding"),
    path("onboarding/<str:user_action>/", AccountsVerification.as_view(), name="accounts_verification"),
    path("notifications/<str:user_type>/", usernotifications.as_view(), name="notifications"),
    # ajax_views
    path("ajax_view/", ajax_view, name="ajax_view"),
    
]
