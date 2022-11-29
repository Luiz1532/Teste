from rest_framework import serializers
from Pessoa.models.pessoa import Pessoa

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ["nome", "email", "celular", "tipo"]