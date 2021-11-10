from saude.models import ListaSintomas, EstadoSaude
from rest_framework import serializers


class ListaSintomasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaSintomas
        fields = '__all__'


class EstadoSaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoSaude
        fields = ['id', 'user', 'estado', 'sintomas']
        depth = 0
