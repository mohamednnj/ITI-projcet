from django import forms
from .models import User

class SignupForm(forms.ModelForm):
    class Meta:
        # email = forms.EmailField(required=True)
        model = User
        fields = ["username", "email","image", "phone", "password"]
        def __init__(self, *args, **kwargs):
            super(SignupForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.label = ''
        widgets = {
            
            'username': forms.TextInput(attrs={
                'placeholder': 'username',
                 
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'email',
                
            }), 
            'phone': forms.Textarea(attrs={
                'placeholder': 'phone number', 
                'class': 'form-control',
                'rows': 1,
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'password',
                
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