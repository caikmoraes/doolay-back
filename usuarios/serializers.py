from rest_framework import serializers
from usuarios import models as usuarios_models
from django.utils.crypto import get_random_string
from django.db.utils import IntegrityError


class AlunoCreateSerializer(serializers.ModelSerializer):
    num_matricula = serializers.CharField(max_length=16, write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = usuarios_models.Usuario
        fields = [
            'first_name',
            'last_name',
            'email',
            'num_matricula',
            'password',
            'data_nascimento',
            'cidade',
            'estado'
        ]

    def create(self, validated_data):
        user_data = {k: validated_data[k] for k in set(list(validated_data.keys())) - {'num_matricula'}}
        user_data['username'] = get_random_string(length=32)
        user = super(AlunoCreateSerializer, self).create(user_data)
        user.set_password(validated_data['password'])
        user.save()
        try:
            usuarios_models.Aluno.objects.create(user=user, num_matricula=validated_data['num_matricula'])
        except IntegrityError:
            raise Exception("unique_constraint")
        return user


class AlunoGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuarios_models.Aluno
        fields = ['num_matricula', 'user']
        depth = 1
