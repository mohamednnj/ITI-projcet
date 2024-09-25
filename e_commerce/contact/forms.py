from django import forms
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'name',
            'class': 'contact-form-control',
        })
    )
    
    email = forms.CharField(
        validators=[EmailValidator()],
        widget=forms.EmailInput(attrs={
            'placeholder': 'email',
            'class': 'contact-form-control',
        })
    )
    
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'placeholder': 'phone',
            'class': 'contact-form-control',
        })
    )
    
    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'subject',
            'class': 'contact-form-control',
        })
    )
    
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'message',
            'class': 'contact-form-control',
            'rows': 3,
        })
    )
