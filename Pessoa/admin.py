from django.contrib import admin
from Pessoa.models.pessoa import Pessoa

@admin.register(Pessoa)

class AdminTask(admin.ModelAdmin):
    list_display = ('nome', 'email', 'celular','tipo')