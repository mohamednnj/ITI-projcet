from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email","image", "phone", "password"]
        widgets = {
            
            'username': forms.TextInput(attrs={
                'placeholder': 'username',
                'class': 'form-control',  
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'email',
                'class': 'form-control',
            }),
            'phone': forms.Textarea(attrs={
                'placeholder': 'message', 
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'password',
                'class': 'form-control',
            }),
        }
        
class loginFrom(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "password"]
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'email',
                'class': 'form-control',
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'password',
                'class': 'form-control',
            }),
        }