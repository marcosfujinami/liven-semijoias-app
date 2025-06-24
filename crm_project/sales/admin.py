from django.contrib import admin
from .models import Sale, SaleItem

class SaleItemInline(admin.TabularInline):
    model = SaleItem
    extra = 1 # Number of empty forms to display
    autocomplete_fields = ['product']
    fields = ('product', 'quantity', 'unit_price', 'total_price')
    readonly_fields = ('total_price',) # Calculated by model save method

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'warehouse', 'sale_date', 'total_amount', 'payment_method')
    list_filter = ('sale_date', 'payment_method', 'warehouse', 'customer')
    search_fields = ('id', 'customer__full_name', 'customer__cpf', 'items__product__name')
    readonly_fields = ('sale_date', 'created_at', 'updated_at', 'total_amount') # total_amount might be calculated
    autocomplete_fields = ['customer', 'warehouse']
    inlines = [SaleItemInline]

    fieldsets = (
        (None, {
            'fields': ('customer', 'warehouse', 'payment_method', 'observations')
        }),
        ('Detalhes da Venda', {
            'fields': ('sale_date', 'total_amount', 'created_at', 'updated_at')
        }),
    )

    # Potentially add a method to calculate total_amount if not done by signals/override save
    # And update it in the admin view if necessary.
    # For now, assuming Sale model's save or signals will handle total_amount update.
