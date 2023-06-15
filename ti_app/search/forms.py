from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['mpn']

        widgets = {
            "mpn": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'MPN'
            })
        }
