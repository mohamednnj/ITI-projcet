from django import forms
from .models import Category

class CategoryFilterForm(forms.Form):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    min_price = forms.DecimalField(
        required=False,
        label="$0",
        min_value=0,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            "class":"form-control"
        })
    )
    max_price = forms.DecimalField(
        required=False,
        label="$10000",
        min_value=0,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            "class":"form-control"
        })
    )