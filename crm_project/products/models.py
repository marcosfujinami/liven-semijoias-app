from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    # Informações Básicas
    name = models.CharField(max_length=255, verbose_name="Nome do Produto")
    sku = models.CharField(max_length=100, unique=True, blank=True, null=True, verbose_name="SKU")
    barcode = models.CharField(max_length=100, unique=True, blank=True, null=True, verbose_name="Código de Barras")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Categoria")
    material = models.CharField(max_length=100, blank=True, null=True, verbose_name="Material")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")

    # Especificações Técnicas
    weight_g = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Peso (g)")
    dimensions = models.CharField(max_length=100, blank=True, null=True, verbose_name="Dimensões (AxLxP cm)") # Assuming Height x Width x Depth
    color = models.CharField(max_length=50, blank=True, null=True, verbose_name="Cor")

    # Precificação
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço de Custo")
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço de Venda")

    # Imagens do Produto
    image_url = models.URLField(max_length=1024, blank=True, null=True, verbose_name="URL da Imagem")

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
