from django import forms
from .models import Order, OrderItem

class OrderForm(forms.ModelForm):
    # Add username, email, and quantity fields to the form
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'readonly': 'readonly'}))
    quantity = forms.IntegerField(label='Quantity', min_value=1, initial=1)  # Allow user to select quantity

    class Meta:
        model = Order
        fields = ['address', 'total_price']  # Existing editable fields (address and total price)

    # Overriding __init__ to auto-fill fields for logged-in user
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the logged-in user from kwargs
        product = kwargs.pop('product', None)  # Get the product from kwargs
        super(OrderForm, self).__init__(*args, **kwargs)

        if user:
            # Auto-fill username and email fields
            self.fields['username'].initial = user.username
            self.fields['email'].initial = user.email
        
        if product:
            # Set total price based on product price (user can change quantity)
            self.fields['total_price'].initial = product.price
            self.fields['total_price'].widget.attrs['readonly'] = True  # Total price should be read-only
