from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'cpf', 'address_city', 'address_state')
    search_fields = ('full_name', 'email', 'cpf', 'address_city')
    list_filter = ('address_state', 'address_city')
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('full_name', 'cpf', 'email', 'phone')
        }),
        ('Endereço', {
            'fields': ('address_street', 'address_number', 'address_complement', 'address_neighborhood', 'address_city', 'address_state', 'address_zip_code')
        }),
    )
