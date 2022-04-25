from django.db import models

# Create your models here.

class Gastos(models.Model):
    nome = models.CharField(max_length=100)
    ocasiao = models.TextField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_de_compra = models.DateField()
    data_criacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'gastos'