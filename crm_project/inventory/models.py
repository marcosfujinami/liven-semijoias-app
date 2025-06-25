from django.db import models
from products.models import Product
from sales_channels.models import SalesChannel # Assuming a warehouse is tied to a sales channel or is a type of sales channel

class Warehouse(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome do Depósito")
    # Link to SalesChannel if a warehouse is essentially a location related to a sales channel
    # If a SalesChannel can BE a warehouse (e.g. a physical store), this might be a OneToOneField or ForeignKey
    sales_channel = models.ForeignKey(SalesChannel, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Local de Venda Associado")
    address = models.TextField(blank=True, null=True, verbose_name="Endereço do Depósito")
    is_default = models.BooleanField(default=False, verbose_name="Depósito Padrão") # Useful for default stock locations

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Produto")
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, verbose_name="Depósito")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Quantidade em Estoque")
    min_quantity = models.PositiveIntegerField(default=0, verbose_name="Quantidade Mínima")
    max_quantity = models.PositiveIntegerField(default=1000, verbose_name="Quantidade Máxima") # Default large value

    last_stocked_date = models.DateTimeField(auto_now=True, verbose_name="Última Atualização de Estoque")

    class Meta:
        unique_together = ('product', 'warehouse') # Each product can only have one entry per warehouse
        verbose_name_plural = "Inventories"

    def __str__(self):
        return f"{self.product.name} em {self.warehouse.name}: {self.quantity}"

class StockTransfer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    from_warehouse = models.ForeignKey(Warehouse, related_name='transfers_out', on_delete=models.CASCADE, verbose_name="Do Depósito")
    to_warehouse = models.ForeignKey(Warehouse, related_name='transfers_in', on_delete=models.CASCADE, verbose_name="Para Depósito")
    quantity = models.PositiveIntegerField(verbose_name="Quantidade Transferida")
    transfer_date = models.DateTimeField(auto_now_add=True, verbose_name="Data da Transferência")
    notes = models.TextField(blank=True, null=True, verbose_name="Observações")

    def __str__(self):
        return f"Transfer of {self.quantity} x {self.product.name} from {self.from_warehouse} to {self.to_warehouse}"
