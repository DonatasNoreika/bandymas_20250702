from django import forms
from django.contrib.auth.forms import UserCreationForm, AdminUserCreationForm
from .models import CustomUser

class CustomUserCreationForm(AdminUserCreationForm):
    class Meta:
        model = CustomUser
        fields = "__all__"