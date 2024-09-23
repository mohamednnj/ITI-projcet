from django.shortcuts import render, redirect
from .forms import UserForm
from django.views.generic import CreateView
from .models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
def profile_view(request):
    return render(request, "accounts/profile.html")
