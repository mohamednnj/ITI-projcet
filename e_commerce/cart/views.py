from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from product.models import *
from .models import *
import json

def add_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')
        quantity = data.get('quantity')

        # Logic to add the product to the cart
        # e.g., Cart.objects.create(product=product, quantity=quantity)

        return JsonResponse({'success': True})

    return JsonResponse({'success': False}, status=400)

def get_cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(customer=request.user).first()
        if cart:
            products = cart.selected_product.all()
            product_data = [
                {
                    'name': product.name,
                    'price': product.price,
                    'image': product.image.url,
                }
                for product in products
            ]
            return JsonResponse({"products": product_data})
    
    return JsonResponse({"error": "Cart not found"}, status=404)