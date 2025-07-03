from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomAdminUserCreationForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomAdminUserCreationForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_employee',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_employee',)}),
    )

# Register your models here.
# admin.site.register(CustomUser)
admin.site.register(CustomUser, CustomUserAdmin)