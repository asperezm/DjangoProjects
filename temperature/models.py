from django.db import models
import uuid

class Temperature(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(verbose_name='Tipo', max_length=20)
    value = models.IntegerField(verbose_name='Valor')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Medicion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.CharField(verbose_name='Fecha', max_length=20)
    origen = models.CharField(verbose_name='Origen', max_length=20)
    valor = models.IntegerField(verbose_name='Valor')
    codigos = models.CharField(verbose_name='Codigos', max_length=25)
    observacion = models.CharField(verbose_name='Observacion', max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)