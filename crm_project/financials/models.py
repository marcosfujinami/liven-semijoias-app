from django.db import models
from sales.models import Sale # Link to sales for income
from django.conf import settings # To link User if expenses are user-specific

class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('income', 'Receita'),
        ('expense', 'Despesa'),
    ]

    description = models.CharField(max_length=255, verbose_name="Descrição")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES, verbose_name="Tipo de Transação")
    transaction_date = models.DateField(verbose_name="Data da Transação")
    # Link to Sale if it's an income from a sale
    sale = models.OneToOneField(Sale, on_delete=models.SET_NULL, null=True, blank=True, related_name='transaction_record', verbose_name="Venda Associada (Receita)")
    # Link to a category for expenses, e.g., Rent, Supplies, Marketing
    category = models.CharField(max_length=100, blank=True, null=True, verbose_name="Categoria (Despesa)")
    notes = models.TextField(blank=True, null=True, verbose_name="Observações")

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_transaction_type_display()} - {self.description} - {self.amount}"

# The following are more for reporting/aggregation rather than direct data entry models,
# but can be represented if complex logic is needed.
# Simpler financial calculations might be done via queries on Transactions.

# class Income(models.Model):
#     # Potentially derived from Transactions of type 'income'
#     # Or could be a separate model if income sources are more complex than just sales
#     pass

# class Expense(models.Model):
#     # Potentially derived from Transactions of type 'expense'
#     pass
