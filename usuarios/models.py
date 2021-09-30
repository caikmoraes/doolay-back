from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    data_nascimento = models.DateTimeField(null=True, blank=True)
    cidade = models.CharField(max_length=128)
    estado = models.CharField(max_length=128)

    REQUIRED_FIELDS = []


class Aluno(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    num_matricula = models.CharField(max_length=16, unique=True)


class Funcionario(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    num_funcional = models.CharField(max_length=16, unique=True)
    setor = models.CharField(max_length=16)
