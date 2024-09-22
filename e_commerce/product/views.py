from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
from .models import Product
# Create your views here.
def product(req):
    products = Product.objects.all()
    return render(req,'shop/index.html',{'products':products} )
>>>>>>> f663142293ed7175adcc32c717e03e02d425199b
