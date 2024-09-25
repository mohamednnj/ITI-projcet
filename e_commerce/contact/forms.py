from django import forms
from .models import Messages

<<<<<<< HEAD

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
=======
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
>>>>>>> 1923cc780f225eec40a7a169675412c0763e85f6
