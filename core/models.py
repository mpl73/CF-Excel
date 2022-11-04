from django.db import models

# Create your models here.
class Cartao(models.Model):
    nome = models.CharField(max_length = 100)
    banco = models.CharField(max_length = 100)
    numero = models.CharField(max_length = 19)
    fechamento = models.DecimalField(max_digits=2, decimal_places=0)
    vencimento = models.DecimalField(max_digits=2, decimal_places=0)

    def __str__(self) -> str:
        return f'{self.nome} | {self.banco}'