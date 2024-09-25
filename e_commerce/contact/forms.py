from django import forms
from .models import Messages


class ContactForm(forms.ModelForm):
    class Meta:
        # email = forms.EmailField(required=True)
        model = Messages
        fields = ["name", "email","phone", "subject", "message"]
    widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'name',
                'class': 'form-control',
                
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'email',
                'class': 'form-control',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'phone',
                'class': 'form-control',
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'subject',
                'class': 'form-control',
                'rows': 1,
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'message',
                'rows': 3,
            }),
    }
