from django.db import models

class SalesChannel(models.Model):
    CHANNEL_CHOICES = [
        ('site', 'Site'),
        ('reseller', 'Revendedora'),
        ('marketplace', 'Marketplace'),
    ]
    name = models.CharField(max_length=100, verbose_name="Nome do Local de Venda")
    type = models.CharField(max_length=20, choices=CHANNEL_CHOICES, verbose_name="Tipo de Local")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"

class Reseller(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Nome Completo da Revendedora")
    cpf = models.CharField(max_length=14, unique=True, help_text="Formato: XXX.XXX.XXX-XX", verbose_name="CPF")
    email = models.EmailField(max_length=255, unique=True, verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefone")

    # Endereço (Modelo Brasileiro)
    address_street = models.CharField(max_length=255, blank=True, null=True, verbose_name="Logradouro")
    address_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Número")
    address_complement = models.CharField(max_length=100, blank=True, null=True, verbose_name="Complemento")
    address_neighborhood = models.CharField(max_length=100, blank=True, null=True, verbose_name="Bairro")
    address_city = models.CharField(max_length=100, blank=True, null=True, verbose_name="Cidade")
    address_state = models.CharField(max_length=2, blank=True, null=True, verbose_name="UF")
    address_zip_code = models.CharField(max_length=9, blank=True, null=True, verbose_name="CEP")

    # Associated sales channel (can be linked if a reseller is a type of sales channel)
    # Or this can be a separate field if a reseller can operate through multiple channels.
    # For now, let's assume a reseller IS a sales channel of type 'reseller'.
    # If a Reseller is always a SalesChannel, consider a OneToOneField to a SalesChannel of type 'reseller'
    # or making Reseller inherit from a base class if fields overlap significantly.
    # For simplicity now, keeping it separate but linked conceptually.
    # sales_channel_info = models.OneToOneField(SalesChannel, on_delete=models.CASCADE, null=True, blank=True, limit_choices_to={'type': 'reseller'})

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
