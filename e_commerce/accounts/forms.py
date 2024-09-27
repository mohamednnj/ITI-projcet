from django import forms
from .models import User

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'password',
        'class': 'form-control',
    }))
    
    class Meta:
        model = User
        fields = ["username",'image', "email", "phone", "password"]  # include all fields
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'username',
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'email',
                'class': 'form-control',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'phone number',
                'class': 'form-control',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        # Optionally, you can add more initialization logic here if needed
        for field_name, field in self.fields.items():
            field.label = ''  # Remove labels for a cleaner UI


class loginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'password',
        'class': 'form-control',
    }))

    class Meta:
        model = User
        fields = ["email", "password"]  # Only email and password for login
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'email',
                'class': 'form-control',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(loginForm, self).__init__(*args, **kwargs)
        # Optionally, you can add more initialization logic here if needed
        for field_name, field in self.fields.items():
            field.label = ''  # Remove labels for a cleaner UI



# from django import forms
# from .models import User

# class SignupForm(forms.ModelForm):
#     class Meta:
#         # email = forms.EmailField(required=True)
#         model = User
#         fields = ["username", "email","image", "phone", "password"]
#         def __init__(self, *args, **kwargs):
#             super(SignupForm, self).__init__(*args, **kwargs)
#             for field_name, field in self.fields.items():
#                 field.label = ''
#         widgets = {
            
#             'username': forms.TextInput(attrs={
#                 'placeholder': 'username',
                 
#             }),
#             'email': forms.EmailInput(attrs={
#                 'placeholder': 'email',
                
#             }), 
#             'phone': forms.Textarea(attrs={
#                 'placeholder': 'phone number', 
#                 'class': 'login-form-control',
#                 'rows': 1,
#             }),
#             'password': forms.PasswordInput(attrs={
#                 'placeholder': 'password',
                
#             }),
#         }
        
# class loginFrom(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ["email", "password"]
#         widgets = {
#             'email': forms.EmailInput(attrs={
#                 'placeholder': 'email',
#                 'class': 'login-form-control',
#             }),
#             'password': forms.PasswordInput(attrs={
#                 'placeholder': 'password',
#                 'class': 'login-form-control',
#             }),
#         }