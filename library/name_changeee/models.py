from uuid import uuid4
from django.db import models

class Pacientes(models.Model):
        id_paciente = models.UUIDField(primary_key=True, default=uuid4, editable=False)
        nome = models.CharField(max_length=255)
        idade = models.IntegerField()
        cpf = models.CharField(max_length=255)
        rg = models.CharField(max_length=255)
        data_nasc = models.DateField()
        sexo = models.CharField(max_length=255)
        signo = models.CharField(max_length=255)
        mae = models.CharField(max_length=255)
        pai = models.CharField(max_length=255)
        email = models.CharField(max_length=255)
        senha = models.CharField(max_length=255)
        cep = models.CharField(max_length=255)
        endereco = models.CharField(max_length=255)
        numero = models.CharField(max_length=255)
        bairro = models.CharField(max_length=255)
        cidade = models.CharField(max_length=255)
        estado = models.CharField(max_length=255)
        telefone_fixo = models.CharField(max_length=255)
        celular = models.CharField(max_length=255)
        altura = models.CharField(max_length=255)
        peso = models.IntegerField
        tipo_sanguineo = models.CharField(max_length=255)
        cor = models.CharField(max_length=255)
