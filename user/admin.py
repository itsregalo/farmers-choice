from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ('basic info', {
            "fields": (
                'username',
                'email',
                'first_name',
                'last_name',
                'profile_pic',
            ),
        }),
        ('category', {
            "fields": (
                'is_superuser',
                'is_staff',
                'is_farmer',
                'is_admin',
            ),
        }),
    )
    
    
admin.site.register(User, CustomUserAdmin)