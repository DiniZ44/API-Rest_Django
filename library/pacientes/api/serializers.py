from dataclasses import fields
from rest_framework import serializers
from pacientes import models

class PacientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Pacientes
        fields = '__all__'