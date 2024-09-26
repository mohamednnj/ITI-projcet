from django.shortcuts import render, get_object_or_404
from category.models import Category
from .models import Product
from accounts.forms import SignupForm, loginForm
# Create your views here.
def product(req):
    categorys = Category.objects.all()
    products = Product.objects.all()
    form = loginForm()
    return render(req,'shop/index.html',{'products':products,'categorys':categorys,'formlogin': form} )

def productdetails(request, product_id):
    categorys = Category.objects.all()
    product = get_object_or_404(Product, id=product_id)
    form = loginForm()
    return render(request, 'shop/productdetails.html', {
        'product': product, 
        'categorys': categorys, 
        'formlogin': form
    })