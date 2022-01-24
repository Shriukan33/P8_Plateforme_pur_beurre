from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import UserRegisterForm


class MyLoginView(LoginView):
    template_name = 'authentification/login.html'


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'authentification/create_account.html'
    success_url = reverse_lazy('authentification:login')
    form_class = UserRegisterForm
    success_message = "Votre compte a été créé avec succès !"


class MyLogoutView(LogoutView):
    """This view de-auth the user, and redirects to login"""
    next_page = reverse_lazy('authentification:login')
