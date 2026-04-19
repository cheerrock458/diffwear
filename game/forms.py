<<<<<<< HEAD
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
=======
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
>>>>>>> 8ada485e1e7684880b2e8dfde05d8b4234635a24
        fields = ['name', 'price', 'category', 'image', 'description']