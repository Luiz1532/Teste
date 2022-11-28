from django.db import models


class Garagem(models.Model):
    
    email = models.CharField('E-mail', max_length=250)
    celular = models.CharField('Número de celular', max_length=250)


def __str__(self):
    return str(self.nome)

class Meta:
    verbose_name = 'Garagem'
    verbose_name_plural = 'Garagens'