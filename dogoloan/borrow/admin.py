from django.contrib import admin

# Register your models here.
from .models import *
@admin.register(BorrowerProfile)
class BorrowerProfileAdmin(admin.ModelAdmin):
    list_display = ('user','employment_status','marital_status','education')
    search_fields = ('user','employment_status','marital_status','education')
    add_fieldsets = (
        (
            None,
        )
    )
