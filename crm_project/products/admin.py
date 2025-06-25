from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'category', 'sale_price', 'cost_price', 'material', 'color')
    list_filter = ('category', 'material', 'color')
    search_fields = ('name', 'sku', 'barcode', 'description')
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('name', 'sku', 'barcode', 'category', 'material', 'description')
        }),
        ('Especificações Técnicas', {
            'fields': ('weight_g', 'dimensions', 'color')
        }),
        ('Precificação', {
            'fields': ('cost_price', 'sale_price')
        }),
        ('Imagens', {
            'fields': ('image_url',)
        }),
    )
