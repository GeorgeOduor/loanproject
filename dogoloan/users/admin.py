from django.contrib import admin
from users.models import User, Profile
from django.utils.translation import gettext_lazy as _



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("msisdn", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("msisdn", "password1", "password2"),
            },
        ),
    )
    list_display = ("msisdn", "first_name", "last_name", "is_staff")
    search_fields = ("msisdn", "first_name", "last_name")
    ordering = ("msisdn",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "gender",  "national_id", "social_reach")
    search_fields = ("user", "first_name", "last_name", "gender","national_id", "social_reach")
    add_fieldsets = (
        (
            None,
        )
    )
    