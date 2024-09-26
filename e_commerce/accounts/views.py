from django.shortcuts import render, redirect
from .forms import SignupForm, loginForm
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages

# Create your views here.
def profile_view(req):
    return render(req, "accounts/profile.html")

def signup(req):
    if req.method == 'POST':
        form_in = SignupForm(req.POST, req.FILES)
        if form_in.is_valid():
            user = form_in.save(commit=False)  # Don't save yet
            user.password = make_password(form_in.cleaned_data['password'])
            form_in.save()  
            form = loginForm()
            messages.error(req, "Sign-up succsess")
            return render(req, 'homePage/index.html', {'formlogin': form})
    else:
        form_in = SignupForm()
    return render(req, 'registration/signup.html', {'form_in': form_in})