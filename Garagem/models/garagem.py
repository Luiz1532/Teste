from django.db import models
from Garagem.models.veiculo import Veiculo


class Garagem(models.Model):
    
    email = models.CharField('E-mail', max_length=250)
    celular = models.CharField('Número de celular', max_length=250)
    veiculos = models.ManyToManyField(Veiculo, default=Veiculo)
    ativa = models.BooleanField('Garagem ativa', default=True)

def __str__(self):
    return str(self.nome)

class Meta:
    verbose_name = 'Garagem'
    verbose_name_plural = 'Garagens'