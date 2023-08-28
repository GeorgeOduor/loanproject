from django.contrib import admin

# Register your models here.
from lenders.models import *

@admin.register(Agents)
class AgentsAdmin(admin.ModelAdmin):
    list_display = ("created_on","supervisor","agent_location","modified_on")
    search_fields = ("created_on","supervisor","agent_location","modified_on")
    add_fieldsets = (
        (
            None,
        )
    )

@admin.register(LenderProfile)
class LenderProfileAdmin(admin.ModelAdmin):
    list_display = ('user','paybillno','brand','date_created')
    search_fields = ('user','paybillno','brand','date_created')
    add_fieldsets = (
        (
            None,
        )
    )

@admin.register(LoanProduct)
class LoanProductAdmin(admin.ModelAdmin):
    list_display = ('lender','name','interest_rate','min_loan_amount','max_loan_amount','repayment_term')
    search_fields = ('lender','name','interest_rate','min_loan_amount','max_loan_amount','repayment_term')
    add_fieldsets = (
        (
            None,
        )
    )

