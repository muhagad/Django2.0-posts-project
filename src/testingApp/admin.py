from django.contrib import admin
from .models import LoginApp

# Register your models here.
class LoginModelAdmin(admin.ModelAdmin):
    list_display = ['username','password','email']

admin.site.register(LoginApp,LoginModelAdmin)
