from django.db import models
from product.models import Product
from accounts.models import User

class Cart(models.Model):
    customer = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    selected_product = models.ManyToManyField(Product)
    
    def __str__(self):
        return f"Cart of {self.customer}"
