from django.db import models

class Supplier(models.Model):
    # Informações do Fornecedor
    name = models.CharField(max_length=255, verbose_name="Nome do Fornecedor")
    cnpj = models.CharField(max_length=18, unique=True, help_text="Formato: XX.XXX.XXX/XXXX-XX", verbose_name="CNPJ") # Assuming XX.XXX.XXX/XXXX-XX
    email = models.EmailField(max_length=255, blank=True, null=True, verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefone")
    contact_person = models.CharField(max_length=255, blank=True, null=True, verbose_name="Pessoa de Contato")

    # Endereço (Modelo Brasileiro)
    address_street = models.CharField(max_length=255, blank=True, null=True, verbose_name="Logradouro")
    address_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Número")
    address_complement = models.CharField(max_length=100, blank=True, null=True, verbose_name="Complemento")
    address_neighborhood = models.CharField(max_length=100, blank=True, null=True, verbose_name="Bairro")
    address_city = models.CharField(max_length=100, blank=True, null=True, verbose_name="Cidade")
    address_state = models.CharField(max_length=2, blank=True, null=True, verbose_name="UF") # Sigla do Estado, ex: SP
    address_zip_code = models.CharField(max_length=9, blank=True, null=True, verbose_name="CEP") # Formato: XXXXX-XXX

    observations = models.TextField(blank=True, null=True, verbose_name="Observações")

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
