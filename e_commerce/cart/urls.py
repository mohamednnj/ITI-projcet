from django.urls import path
from .views import *

urlpatterns = [
    path('order/<int:product_id>/', create_order, name='create_order'), 
    # path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),

    path('', cart, name="cart"),
    path('delete', cart_summary, name="cart_delete"),
    path('update', cart_summary, name="cart_update"),
    path('convert-cart-to-order/', convert_cart_to_order, name='convert_cart_to_order'),
]
