from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

class UsuarioManager(BaseUserManager):
    def create_user(self, num_identificacao, tipo_usuario, name=None, password=None, **extra_fields):
        user = self.model(num_identificacao=num_identificacao, tipo_usuario=tipo_usuario, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, num_identificacao, tipo_usuario, name, password=None, **extra_fields):
        user = self.create_user(num_identificacao=num_identificacao,
                                tipo_usuario=tipo_usuario,
                                name=name,
                                password=password,
                                **extra_fields)
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    name = models.CharField(max_length=256, null=True, blank=True, default="none informed")
    data_nascimento = models.DateField(null=True, blank=True)
    cidade = models.CharField(max_length=128, default="none informed")
    estado = models.CharField(max_length=128, default="none informed")
    num_identificacao = models.CharField(max_length=8, unique=True, primary_key=True)
    tipo_usuario = models.CharField(max_length=3, choices=[
        ("ALU", "Aluno"),
        ("FUN", "Funcionario")
    ])
    setor = models.ForeignKey('setores.Setor', on_delete=models.DO_NOTHING, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = "num_identificacao"
    REQUIRED_FIELDS = ["tipo_usuario", "setor", "name"]

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.num_identificacao
