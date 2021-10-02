from setores.models import Setor
from setores import serializers as setores_serializers
from rest_framework import viewsets


class SetorViewSet(viewsets.ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = setores_serializers.SetorSerializer
