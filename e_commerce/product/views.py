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
    
def product_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)  # Get the category by id
    products = Product.objects.filter(category=category)  # Get all products related to the category
    return render(request, 'shop/product_by_category.html', {'category': category, 'products': products})    

