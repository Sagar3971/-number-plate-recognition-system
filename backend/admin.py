from django.contrib import admin

# Register your models here.
from .models import User_info

@admin.register(User_info)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone', 'vehicle_number', 'vehicle_type','username', 'password')

