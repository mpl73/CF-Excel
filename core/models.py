from django.db import models

# Create your models here.
class Cartao(models.Model):
    nome = models.CharField(max_length = 100)
    banco = models.CharField(max_length = 100)
    numero = models.CharField(max_length = 19)
    fatura_atual = models.DecimalField(max_digits=9, decimal_places=2)
    fatura_passada = models.DecimalField(max_digits=9, decimal_places=2)
    limite = models.DecimalField(max_digits=9, decimal_places=2)
    fechamento = models.DecimalField(max_digits=2, decimal_places=0)
    vencimento = models.DecimalField(max_digits=2, decimal_places=0)

    class Meta:
        verbose_name = 'Cartão'
        verbose_name_plural = 'Cartões'

    def __str__(self) -> str:
        return f'{self.nome} | {self.banco}'

class Gasto(models.Model):
    data = models.DateField()
    motivo = models.CharField(max_length = 100)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    tipo = models.CharField(max_length = 10)
    forma = models.CharField(max_length = 50)
    cartao = models.ForeignKey("Cartao", on_delete=models.CASCADE)
    mes = models.DecimalField(max_digits=2, decimal_places=0)

    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'

    def __str__(self) -> str:
        return f'Mês: {self.mes} | Valor: {self.valor} | Tipo : {self.tipo}'