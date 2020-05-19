from django.shortcuts import render

from rest_framework import viewsets
from .models import Temperature
from .serializers import TemperatureSerializer
from .serializers import MedicionSerializer
from .models import Medicion

class TemperatureViewSet(viewsets.ModelViewSet):
    queryset = Temperature.objects.all().order_by('-created')
    serializer_class = TemperatureSerializer

class MedicionViewSet(viewsets.ModelViewSet):
    queryset = Medicion.objects.all().order_by('-created')
    serializer_class = MedicionSerializer