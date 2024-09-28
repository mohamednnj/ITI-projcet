from django.shortcuts import render, redirect
from .forms import SignupForm, loginForm
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from cart.models import Order

# Create your views here.
def profile_view(req):
    if req.user.is_authenticated:
        orders = Order.objects.filter(user=req.user)
    else:
        orders = None  # Or you could redirect to login page or show a message
    
    return render(req, "accounts/profile.html",{'orders': orders})

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

