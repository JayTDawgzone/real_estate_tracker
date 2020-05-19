from django.contrib import admin

from .models import Listing, Maintenance, Rental, Insurance, Expense, Mortgage

class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'status', 'type','city', 'state', 'asking_price', 'list_date', 'manager')
  list_display_links = ('id', 'title')
  list_filter = ('status','city','state', 'type')
  list_editable = ('is_published','status', 'asking_price')
  search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'asking_price')
  list_per_page = 25

class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing', 'title', 'repair_date', 'cost', 'repair_status')
    list_display_links = ('id', 'listing')
    list_filter = ('repair_status', 'listing')
    list_editable = ('repair_status',)
    list_per_page = 25

class RentalAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing', 'lease_number', 'rental_status','rental_price', 'security_deposit', 'tenant_name', 'tenant_phone')
    list_display_links = ('id', 'listing', 'lease_number')
    list_filter = ('listing', 'tenant_name')
    list_editable = ('rental_status', 'rental_price', 'security_deposit')
    list_per_page = 25

class InsuranceAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing', 'insurance_company','annual_pmt', 'effective_start_date', 'effective_end_date', 'liability_amt', 'replacement_amt')
    list_display_links = ('id', 'listing',)
    list_filter = ('listing', 'insurance_company')
    list_editable = ('annual_pmt', 'effective_start_date', 'effective_end_date')
    list_per_page = 25

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing', 'expense_type','vendor_name', 'responsibility', 'autopay')
    list_display_links = ('id', 'listing',)
    list_filter = ('listing', 'expense_type', 'vendor_name', 'responsibility')
    list_editable = ('responsibility', 'autopay')
    list_per_page = 25

class MortgageAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing', 'lender','loan_number', 'monthly_pmt', 'principal', 'interest', 'impound')
    list_display_links = ('id', 'listing',)
    list_filter = ('listing', 'lender')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
admin.site.register(Maintenance, MaintenanceAdmin)
admin.site.register(Rental, RentalAdmin)
admin.site.register(Insurance, InsuranceAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Mortgage, MortgageAdmin)
