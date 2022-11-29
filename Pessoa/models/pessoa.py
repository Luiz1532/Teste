from django.db import models
from Garagem.models.garagem import Garagem


class Pessoa(models.Model):

    TIPO_CHOICES = [
        (1, 'Administrador'),
        (2, 'Consumidor'),
    ]
    garagem = models.OneToOneField(Garagem, on_delete=models.CASCADE, default=Garagem)
    nome = models.CharField('Nome da pessoa', max_length=250)
    email = models.CharField('E-mail', max_length=250)
    celular = models.CharField('Número de celular', max_length=250)
    tipo = models.IntegerField('Tipo', choices=TIPO_CHOICES)


def __str__(self):
    return str(self.nome)

class Meta:
    verbose_name = 'Pessoa'
    verbose_name_plural = 'Pessoas'