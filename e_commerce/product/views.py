from django.shortcuts import render

# Create your views here.
from .models import Product
# Create your views here.
def product(req):
    products = Product.objects.all()
    return render(req,'shop/index.html',{'products':products} )