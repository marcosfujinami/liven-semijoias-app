from django.db import models
from products.models import Product

class Collection(models.Model):
    STATUS_CHOICES = [
        ('active', 'Ativo'),
        ('inactive', 'Inativo'),
    ]
    name = models.CharField(max_length=255, verbose_name="Nome da Coleção")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")
    season = models.CharField(max_length=50, blank=True, null=True, verbose_name="Temporada") # Ex: Verão, Inverno, Dia das Mães
    year = models.PositiveIntegerField(blank=True, null=True, verbose_name="Ano")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active', verbose_name="Status")
    products = models.ManyToManyField(Product, blank=True, related_name="collections", verbose_name="Produtos da Coleção")

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
