from rest_framework import viewsets
from pacientes.api import serializers
from pacientes import models

class PacientesViewset(viewsets.ModelViewSet):
    serializer_class = serializers.PacientesSerializers
    queryset = models.Pacientes.objects.all()