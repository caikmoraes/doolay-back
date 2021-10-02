from rest_framework import serializers
from setores.models import Setor


class SetorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Setor
        fields = '__all__'
