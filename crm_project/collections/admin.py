from django.contrib import admin
from .models import Collection

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'season', 'year', 'status', 'product_count')
    list_filter = ('status', 'season', 'year')
    search_fields = ('name', 'description')
    filter_horizontal = ('products',) # For easier selection of many-to-many products

    def product_count(self, obj):
        return obj.products.count()
    product_count.short_description = 'Qtd. Produtos'
