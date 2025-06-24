from django.contrib import admin
from .models import Warehouse, Inventory, StockTransfer

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'sales_channel', 'address', 'is_default')
    list_filter = ('is_default', 'sales_channel')
    search_fields = ('name', 'address')

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'warehouse', 'quantity', 'min_quantity', 'max_quantity', 'last_stocked_date')
    list_filter = ('warehouse', 'product__category')
    search_fields = ('product__name', 'warehouse__name')
    autocomplete_fields = ['product', 'warehouse'] # For easier selection

@admin.register(StockTransfer)
class StockTransferAdmin(admin.ModelAdmin):
    list_display = ('product', 'from_warehouse', 'to_warehouse', 'quantity', 'transfer_date')
    list_filter = ('transfer_date', 'from_warehouse', 'to_warehouse')
    search_fields = ('product__name',)
    autocomplete_fields = ['product', 'from_warehouse', 'to_warehouse']
    readonly_fields = ('transfer_date',)
