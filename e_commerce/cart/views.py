from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, Order, OrderItem
from product.models import Product
from .forms import OrderForm
from django.contrib.auth.decorators import login_required

@login_required  # Ensure the user is logged in
def create_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Get the clicked product

    if request.method == 'POST':
        form = OrderForm(request.POST, user=request.user, product=product)  # Pass user and product to the form
        if form.is_valid():
            # Create the order
            order = form.save(commit=False)
            order.user = request.user

            # Get the selected quantity from the form
            quantity = form.cleaned_data['quantity']

            # Calculate total price based on quantity and product price
            order.total_price = product.price * quantity
            order.save()

            # Create an order item
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity
            )

            return redirect('product')  # Redirect to success page
    else:
        form = OrderForm(user=request.user, product=product)  # Provide the user and product to the form for auto-filling
    
    return render(request, 'cart/order_form.html', {'form': form, 'product': product})

def cart_summary(request):
    return render(request, "cart/cart_summary.html", {})




def cart_add(request):
    pass
def cart_delete(request):
    pass
def cart_update(request):
    pass
