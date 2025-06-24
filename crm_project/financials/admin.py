from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'transaction_type', 'transaction_date', 'sale', 'category')
    list_filter = ('transaction_type', 'transaction_date', 'category')
    search_fields = ('description', 'sale__id', 'category')
    autocomplete_fields = ['sale']
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('description', 'amount', 'transaction_type', 'transaction_date')
        }),
        ('Detalhes Adicionais', {
            'fields': ('sale', 'category', 'notes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',) # Collapsible section
        }),
    )
