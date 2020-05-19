from rest_framework import serializers
from .models import Temperature
from .models import Medicion

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ('id', 'type', 'value')

class MedicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicion
        fields = ('id', 'fecha', 'origen', 'valor', 'codigos', 'observacion')