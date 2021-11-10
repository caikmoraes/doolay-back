from saude.models import ListaSintomas, EstadoSaude
from rest_framework import serializers


class ListaSintomasSerializer(serializers.ModelSerializer):
    model = ListaSintomas
    fields = '__all__'


class EstadoSaudeSerializer(serializers.ModelSerializer):
    model = EstadoSaude
    fields = '__all__'
    depth = 1