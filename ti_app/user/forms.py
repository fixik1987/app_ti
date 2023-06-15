from .models import User
from django.forms import ModelForm
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, IntegerField


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password', 'mail', 'admission']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'User name'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }),
            "mail": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'E-Mail'
            })
        }
