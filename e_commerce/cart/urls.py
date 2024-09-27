from django.urls import path
from . import views
from .views import add_to_cart

urlpatterns = [
    path('get_cart/', views.get_cart, name='get_cart'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
]



