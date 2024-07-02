from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.*
# @admin.register(Park)
# class UserAdmin(admin.ModelAdmin):
#     list_display=('id','noplate')
    
@admin.register(Pi)
class UserAdmin(admin.ModelAdmin):
    list_display=('pic','iii')    

@admin.register(Tasbir)
class UserAdmin(admin.ModelAdmin):
    list_display=('user','tasbir')    

@admin.register(FineDetail)
class FineDetailAdmin(admin.ModelAdmin):
    list_display = ['traffic_officer', 'vehicle_number', 'owner_email', 'owner_name', 'location', 'time', 'fine_types', 'other_fine', 'common_amount', 'fine_reason', 'created_at', 'paid']
    list_filter = ['traffic_officer', 'time', 'created_at', 'paid']
    search_fields = ['vehicle_number', 'owner_email', 'owner_name', 'location', 'fine_types', 'fine_reason']

@admin.register(Paaark)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','noplate','category','email_address')