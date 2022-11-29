from django.contrib import admin
from Garagem.models.garagem import Garagem
from Garagem.models.veiculo import Veiculo

@admin.register(Garagem)

class AdminTask(admin.ModelAdmin):
    list_display = ('email', 'celular', 'ativa')

@admin.register(Veiculo)

class AdminTask(admin.ModelAdmin):
    list_display = ('data_fabricacao', 'modelo', 'cor', 'tipo')