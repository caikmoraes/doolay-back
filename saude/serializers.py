from saude.models import ListaSintomas, EstadoSaude, Sintoma, EstadoSintomaItem
from rest_framework import serializers


class ListaSintomasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaSintomas
        fields = '__all__'


class EstadoSaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoSaude
        fields = ['id', 'user', 'estado']
        depth = 0

class SintomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sintoma
        fields = ['id', 'nome']


class EstadoSintomaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoSintomaItem
        fields = ['id', 'sintoma', 'estado_saude', 'apresenta']


class EstadoSaudeNestedSerializer(serializers.ModelSerializer):
    sintomas = serializers.SerializerMethodField()
    date = serializers.DateTimeField(format="%Y-%m-%d")

    def get_sintomas(self, item):
        objects = EstadoSintomaItem.objects.filter(estado_saude=EstadoSaude.objects.get(pk=item.pk))
        serializer = EstadoSintomaItemSerializer(objects, many=True)
        return serializer.data

    class Meta:
        model = EstadoSaude
        fields = ['id', 'user', 'estado', 'sintomas', 'date']