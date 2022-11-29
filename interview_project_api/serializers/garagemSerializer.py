from rest_framework import serializers
from Garagem.models.garagem import Garagem

class GaragemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garagem
        fields = ["email", "celular", "veiculos", "ativa"]