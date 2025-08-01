from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
# Create your views here.

from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    template_name = 'login.html'




class CustomRegisterView(CreateView):
    model = User
    fields = ['username', 'password']
    template_name = 'register.html'
    success_url = reverse_lazy('signin')