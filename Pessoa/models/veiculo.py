from django.db import models
from Garagem.models.garagem import Garagem


class Veiculo(models.Model):
    
    TIPO_CHOICES = [
        (1, 'Carro'),
        (2, 'Moto'),
    ]
    data_fabricacao = models.DateField('Data de fabricação')
    modelo = models.CharField('Modelo do veículo', max_length=250, null=True, blank=True)
    cor = models.CharField('Cor do veículo', max_length=250, null=True, blank=True)
    tipo = models.IntegerField('Tipo', choices=TIPO_CHOICES)
    garagem = models.ForeignKey(Garagem, on_delete=models.CASCADE)


def __str__(self):
    return str(self.nome)

class Meta:
    verbose_name = 'Veiculo'
    verbose_name_plural = 'Veiculos'