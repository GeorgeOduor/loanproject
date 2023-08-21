from django.contrib import admin

# Register your models here.
from management.models import *

@admin.register(BorrowerProfile)
class BorrowerProfileAdmin(admin.ModelAdmin):
    list_display = ('user','agent','employment_status','marital_status','education')
    search_fields = ('user','agent','employment_status','marital_status','education')
    add_fieldsets = (
        (
            None,
        )
    )
