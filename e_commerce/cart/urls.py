from django.urls import path
from . import views

urlpatterns = [
    path('order/<int:product_id>/', views.create_order, name='create_order'), 
]