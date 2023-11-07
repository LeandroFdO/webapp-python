from django.db import models
from decimal import Decimal


class webapp_python_produtos(models.Model):
    nome = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=20, decimal_places=4, default=0.0)
    tipo = models.CharField(max_length=200)
    fornecedor = models.CharField(max_length=200)
    quantidade = models.IntegerField(default=0)
    def __str__(self):
        return self.nome