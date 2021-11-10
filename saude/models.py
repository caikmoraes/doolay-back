from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ListaSintomas(models.Model):
    falta_ar = models.BooleanField()
    cansaco = models.BooleanField()
    febre = models.BooleanField()
    calafrios = models.BooleanField()
    tosse = models.BooleanField()
    dor_garganta = models.BooleanField()
    dor_cabeca = models.BooleanField()
    dor_peito = models.BooleanField()
    perda_olfato = models.BooleanField()
    perda_paladar = models.BooleanField()
    diarreia = models.BooleanField()
    coriza = models.BooleanField()
    espirros = models.BooleanField()


class EstadoSaude(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.CharField(max_length=12, choices=[
        ("OK", "Bem"),
        ("NOK", "Não muito bem")
    ])
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    sintomas = models.ForeignKey(ListaSintomas, null=True, blank=True, on_delete=models.CASCADE)
