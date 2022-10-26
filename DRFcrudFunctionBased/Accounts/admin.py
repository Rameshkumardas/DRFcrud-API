from django.contrib import admin
from Accounts.models import UserRegistation

# Register your models here.
@admin.register(UserRegistation)
class UserRegistationAdmin(admin.ModelAdmin):
    list_display = ['id','full_name','email','pNumber','password']

 