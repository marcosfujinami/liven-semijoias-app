from django.contrib import admin
from .models import SalesChannel, Reseller

@admin.register(SalesChannel)
class SalesChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'description')
    list_filter = ('type',)
    search_fields = ('name', 'description')

@admin.register(Reseller)
class ResellerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'cpf', 'address_city')
    search_fields = ('full_name', 'email', 'cpf')
    # Consider linking to SalesChannel if that relationship is formalized
    # list_filter = ('sales_channel_info__type',)
