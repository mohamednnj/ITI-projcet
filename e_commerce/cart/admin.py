from django.contrib import admin
from django.contrib import admin
from .models import *

# Register your models here.

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    inlines = [CartItemInline]

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'total_price', 'status')
    list_filter = ('status',)
    inlines = [OrderItemInline]

admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)

