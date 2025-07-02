from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser

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

class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'profile.html'
    success_url = reverse_lazy('profile')
    context_object_name = "user"

    def get_object(self, queryset=None):
        return self.request.user