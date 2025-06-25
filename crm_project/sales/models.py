from django.db import models
from products.models import Product
from customers.models import Customer
from inventory.models import Warehouse # Sales occur from a specific warehouse/stock location

class Sale(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('pix', 'Pix'),
        ('cash', 'Dinheiro'),
        ('credit_card', 'Cartão de Crédito'),
        ('debit_card', 'Cartão de Débito'),
        ('transfer', 'Transferência Bancária'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Cliente")
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT, verbose_name="Depósito/Local de Venda") # Don't delete warehouse if sales exist
    sale_date = models.DateTimeField(auto_now_add=True, verbose_name="Data da Venda")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Valor Total")
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, verbose_name="Forma de Pagamento")
    observations = models.TextField(blank=True, null=True, verbose_name="Observações")

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Venda #{self.id} - {self.customer.full_name if self.customer else 'Cliente Avulso'} - {self.sale_date.strftime('%d/%m/%Y')}"

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, related_name='items', on_delete=models.CASCADE, verbose_name="Venda")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Produto") # Don't delete product if it's in a sale
    quantity = models.PositiveIntegerField(verbose_name="Quantidade")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço Unitário (na venda)") # Price at the time of sale
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço Total do Item")

    def save(self, *args, **kwargs):
        self.total_price = self.unit_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} na Venda #{self.sale.id}"
