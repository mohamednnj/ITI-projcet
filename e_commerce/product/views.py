from django.shortcuts import render
from category.models import Category
from .models import Product
from accounts.forms import SignupForm, loginForm
# Create your views here.
def product(req):
    categorys = Category.objects.all()
    products = Product.objects.all()
    form = loginForm()
    return render(req,'shop/index.html',{'products':products,'categorys':categorys,'formlogin': form} )

def productdetails(request):
    return render(request, 'shop/productdetails.html')