from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from saude.models import ListaSintomas, EstadoSaude
from saude.serializers import EstadoSaudeSerializer, ListaSintomasSerializer


class ListaSintomasViewSet(viewsets.ModelViewSet):
    queryset = ListaSintomas.objects.all()
    serializer_class = ListaSintomasSerializer


class EstadoSaudeViewSet(viewsets.ModelViewSet):
    queryset = EstadoSaude.objects.all()
    serializer_class = EstadoSaudeSerializer


class EstadoSaudeDetail(APIView):
    queryset = EstadoSaude.objects.all()
    serializer_class = EstadoSaudeSerializer

    def get(self, request, user_pk, format=None):
        obj = self.queryset.filter(user_id=user_pk)
        serializer = self.serializer_class(obj, many=True)
        return Response(serializer.data)
