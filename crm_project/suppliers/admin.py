from django.contrib import admin
from .models import Supplier

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'cnpj', 'email', 'phone', 'contact_person', 'address_city')
    search_fields = ('name', 'cnpj', 'email', 'contact_person')
    list_filter = ('address_state', 'address_city')
    fieldsets = (
        ('Informações do Fornecedor', {
            'fields': ('name', 'cnpj', 'email', 'phone', 'contact_person')
        }),
        ('Endereço', {
            'fields': ('address_street', 'address_number', 'address_complement', 'address_neighborhood', 'address_city', 'address_state', 'address_zip_code')
        }),
        ('Outros', {
            'fields': ('observations',)
        }),
    )
