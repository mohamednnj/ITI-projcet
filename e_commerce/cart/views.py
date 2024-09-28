from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, Order, OrderItem, CartItem
from product.models import Product
from .forms import OrderForm
from django.contrib.auth.decorators import login_required

@login_required
def create_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = OrderForm(request.POST, user=request.user, product=product)  
        if form.is_valid():
            # Create the order
            order = form.save(commit=False)
            order.user = request.user

            quantity = form.cleaned_data['quantity']

            order.total_price = product.price * quantity
            order.save()

            # Create an order item
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity
            )

            return redirect('product')  
    else:
        form = OrderForm(user=request.user, product=product)  
    
    return render(request, 'cart/order_form.html', {'form_order': form, 'product': product})



def cart_summary(request):
    return render(request, "cart/cart_summary.html", {})


@login_required(login_url='/login/') 
# ====================================

# def add_to_cart(request, product_id):
#     # Get the quantity from the query parameters (GET)
#     quantity = int(request.GET.get('quantity', 1))  # Default to 1 if not found
#     product = get_object_or_404(Product, id=product_id)
    
#     # Check if the user is authenticated
#     if request.user.is_authenticated:
#         # Get or create the user's cart
#         cart, created = Cart.objects.get_or_create(user=request.user)
        
#         # Add the product to the cart with the specified quantity
#         cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
#         cart_item.quantity += quantity
#         cart_item.save()
        
#         # Redirect to the cart page or any other page
#         return redirect('cart_detail')
#     else:
#         # If the user is not logged in, redirect to the login page
#         return redirect('login')

# ================================

 
# def add_to_cart(request, product_id):

#     product = get_object_or_404(Product, id=product_id)
#     quantity = int(request.GET.get('quantity', 1))
#     cart, created = Cart.objects.get_or_create(user=request.user)
#     cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

#     if not item_created:
#         cart_item.quantity += quantity
#         cart_item.save()
#     else:
#         cart_item.quantity = quantity
#         cart_item.save()

#     return redirect('cart')

# =======================================


def add_to_cart(request, product_id):
    # Get the quantity from the query parameters (GET)
    quantity = int(request.GET.get('quantity'))  # Default to 1 if not found
    product = get_object_or_404(Product, id=product_id)
    
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Get or create the user's cart
        cart, created = Cart.objects.get_or_create(user=request.user)
        
        # Add the product to the cart with the specified quantity
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += quantity
        cart_item.save()
        
        # Redirect to the cart page or any other page
        return redirect('cart')  # Change this to your cart view
    else:
        # If the user is not logged in, redirect to the login page
        return redirect('login')

# =====================================================
@login_required(login_url='/login/')
def cart(request):
    # Get the user's cart
    cart = Cart.objects.get(user=request.user)
    
    # Get all items in the cart
    cart_items = cart.items.all()
    
    return render(request, 'cart/cart_view.html', {'cart_items': cart_items})



def convert_cart_to_order(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            order = Order.objects.create(user=request.user, total_price=0, address="Your Address Here") 

            total_price = 0
            
            for item in cart.items.all():
                OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
                total_price += item.product.price * item.quantity

            order.total_price = total_price
            order.save()

            cart.items.all().delete()
            
            return redirect('profile') 
    else:
        return redirect('login')  