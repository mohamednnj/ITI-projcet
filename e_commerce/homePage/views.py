from .models import Banner
from django.contrib.auth import authenticate, login
from accounts.models import User
from accounts.forms import loginForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.urls import reverse
from product.models import Product
# Create your views here.
  
    
def home_page(req):
    recent_added_product = Product.objects.all()[:15]
    form = loginForm()
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
            return render(req,'homePage/index.html',{'banner':banner, "formlogin":form, 'products_recintly_added':recent_added_product} )
    else:
        return render(req,'homePage/index.html',{'banner':banner, "formlogin":form, 'products_recintly_added':recent_added_product} )

