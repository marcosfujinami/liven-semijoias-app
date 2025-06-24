from django import forms
from .models import Product, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'sku', 'barcode', 'category', 'material', 'description',
            'weight_g', 'dimensions', 'color',
            'cost_price', 'sale_price', 'image_url'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'sku': forms.TextInput(attrs={'class': 'form-control'}),
            'barcode': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'material': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'weight_g': forms.NumberInput(attrs={'class': 'form-control'}),
            'dimensions': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'cost_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'sale_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control'}),
        }
