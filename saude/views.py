from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from saude.models import ListaSintomas, EstadoSaude
from saude.serializers import EstadoSaudeSerializer, ListaSintomasSerializer
from django.http import Http404


# Create your views here.
class ListaSintomasList(APIView):
    serializer = ListaSintomasSerializer

    def post(self, request, format=None):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListaSintomasDetail(APIView):
    model = ListaSintomas
    serializer = ListaSintomasSerializer

    def get_object_by_pk(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        obj = self.get_object_by_pk(pk)
        serializer = self.serializer(obj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        obj = self.get_object_by_pk(pk)
        serializer = self.serializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        obj = self.get_object_by_pk(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EstadoSaudeList(APIView):
    serializer = EstadoSaudeSerializer

    def post(self, request, format=None):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EstadoSaudePerUser(APIView):
    model = EstadoSaude
    serializer = EstadoSaudeSerializer

    def get_object_by_user(self, user_pk):
        try:
            return self.model.objects.filter(user_id=user_pk)
        except self.model.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        obj = self.get_object_by_user(pk)
        serializer = self.serializer(obj, many=True)
        return Response(serializer.data)


class EstadoSaudeDetail(APIView):
    model = EstadoSaude
    serializer = EstadoSaudeSerializer

    def get_object_by_pk(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        obj = self.get_object_by_pk(pk)
        serializer = self.serializer(obj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        obj = self.get_object_by_pk(pk)
        serializer = self.serializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        obj = self.get_object_by_pk(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)