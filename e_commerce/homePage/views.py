from .models import Banner
from django.contrib.auth import authenticate, login
from accounts.models import User
from accounts.forms import loginFrom
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.urls import reverse
# Create your views here.
  
    
def home_page(req):
    form = loginFrom()
    banner = Banner.objects.all()
    if req.method == 'POST':
        email = req.POST['email']
        password = req.POST['password']
        user = authenticate(req, username=email, password=password)
        if user is not None:
            login(req, user)
            url = reverse('homePage')
            return redirect(url)  
        else:
            # If authentication fails, display an error message
            messages.error(req, "Invalid email or password")
            return render(req,'homePage/index.html',{'banner':banner,"form":form} )
    else:
        return render(req,'homePage/index.html',{'banner':banner,"form":form} )

