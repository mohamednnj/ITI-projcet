from django.shortcuts import render, get_object_or_404
from category.models import Category
from .models import Product
from category.forms import CategoryFilterForm
from accounts.forms import SignupForm, loginForm

# Create your views here.
def product(req):
    categorys = Category.objects.all()
    products = Product.objects.all()
    form_query = CategoryFilterForm(req.GET or None)

    if form_query.is_valid():
        selected_categories = form_query.cleaned_data.get('categories')
        min_price = form_query.cleaned_data.get('min_price')
        max_price = form_query.cleaned_data.get('max_price')

        if selected_categories:
            products = products.filter(category__in=selected_categories)
        
        if min_price is not None:
            products = products.filter(price__gte=min_price)
        if max_price is not None:
            products = products.filter(price__lte=max_price)

    form = loginForm()
    context = {
        'products': products,
        'form_query': form_query,
        'categorys':categorys,
        'formlogin': form,
    }
    return render(req,'shop/index.html',context=context)

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

