from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

    # fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields': ('is_employee',)}),
    # )
    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     (None, {'fields': ('is_employee',)}),
    # )
