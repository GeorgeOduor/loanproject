from django.contrib import admin
from users.models import User, Profile,Agents
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
    list_display = ("user", "first_name", "last_name", "gender",  "nationa_id", "address", "birth_date")
    search_fields = ("user", "first_name", "last_name", "gender","nationa_id", "address", "birth_date")
    add_fieldsets = (
        (
            None,
        )
    )

@admin.register(Agents)
class AgentsAdmin(admin.ModelAdmin):
    list_display = ("created_on","supervisor","agent_location","modified_on")
    search_fields = ("created_on","supervisor","agent_location","modified_on")
    add_fieldsets = (
        (
            None,
        )
    )

