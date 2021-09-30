from usuarios.serializers import AlunoCreateSerializer, AlunoGetSerializer
from usuarios.models import Usuario, Aluno
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import Http404


class AlunosCreate(APIView):
    queryset = Usuario.objects.all()
    serializer_class = AlunoCreateSerializer
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():

            try:
                serializer.save()
            except Exception:
                return Response({"error": "Número de matrícula não é único"})

            return Response(request.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlunosDetail(APIView):
    def get_object(self, pk):
        try:
            return Aluno.objects.get(num_matricula=pk)
        except Aluno.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        aluno = self.get_object(pk)
        serializer = AlunoGetSerializer(aluno)
        return Response(serializer.data)


@api_view(['POST'])
def validate_aluno(request):
    data = request.data

    try:
        data['num_matricula']
    except KeyError:
        return Response({"error": "Não há número de matrícula"})

    try:
        data['password']
    except KeyError:
        return Response({"error": "Favor informe a senha"})

    num_matricula = data['num_matricula']
    password = data['password']

    try:
        aluno = Aluno.objects.get(num_matricula=num_matricula)
        user = aluno.user
    except Aluno.DoesNotExist:
        return Response({"error": "Aluno não existe"})

    if user.check_password(password):
        return Response({"message": "OK"})
    else:
        return Response({"message": "Senha incorreta."})
