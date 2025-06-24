from django.db import models

class Customer(models.Model):
    # Informações do Cliente
    full_name = models.CharField(max_length=255, verbose_name="Nome Completo")
    cpf = models.CharField(max_length=14, unique=True, help_text="Formato: XXX.XXX.XXX-XX", verbose_name="CPF") # Assuming XXX.XXX.XXX-XX
    email = models.EmailField(max_length=255, unique=True, verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefone") # (XX) XXXXX-XXXX or (XX) XXXX-XXXX

    # Endereço (Modelo Brasileiro)
    address_street = models.CharField(max_length=255, blank=True, null=True, verbose_name="Logradouro")
    address_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Número")
    address_complement = models.CharField(max_length=100, blank=True, null=True, verbose_name="Complemento")
    address_neighborhood = models.CharField(max_length=100, blank=True, null=True, verbose_name="Bairro")
    address_city = models.CharField(max_length=100, blank=True, null=True, verbose_name="Cidade")
    address_state = models.CharField(max_length=2, blank=True, null=True, verbose_name="UF") # Sigla do Estado, ex: SP
    address_zip_code = models.CharField(max_length=9, blank=True, null=True, verbose_name="CEP") # Formato: XXXXX-XXX

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
