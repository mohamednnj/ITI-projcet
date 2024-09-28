from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('order/<int:product_id>/', views.create_order, name='create_order'), 
=======
    path('', views.cart_summary, name="cart_summary"),
    path('add', views.cart_summary, name="cart_add"),
    path('delete', views.cart_summary, name="cart_delete"),
    path('update', views.cart_summary, name="cart_update"),
>>>>>>> edc58cd2aa223de0d64ba8d625a91adcfef0110b
]