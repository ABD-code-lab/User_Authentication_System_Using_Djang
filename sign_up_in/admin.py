from django.contrib import admin
from .models import Sign_Up_In

class Sign_Up_In_Admin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'password')
    
admin.site.register(Sign_Up_In, Sign_Up_In_Admin)