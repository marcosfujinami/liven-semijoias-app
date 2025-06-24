from django import forms
from .models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = [
            'name', 'cnpj', 'email', 'phone', 'contact_person',
            'address_street', 'address_number', 'address_complement',
            'address_neighborhood', 'address_city', 'address_state', 'address_zip_code',
            'observations'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'XX.XXX.XXX/XXXX-XX'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(XX) XXXXX-XXXX'}),
            'contact_person': forms.TextInput(attrs={'class': 'form-control'}),
            'address_street': forms.TextInput(attrs={'class': 'form-control'}),
            'address_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address_complement': forms.TextInput(attrs={'class': 'form-control'}),
            'address_neighborhood': forms.TextInput(attrs={'class': 'form-control'}),
            'address_city': forms.TextInput(attrs={'class': 'form-control'}),
            'address_state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UF (ex: SP)'}),
            'address_zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'XXXXX-XXX'}),
            'observations': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
