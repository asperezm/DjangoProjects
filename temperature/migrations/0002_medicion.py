# Generated by Django 3.0.3 on 2020-05-19 17:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('temperature', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha', models.CharField(max_length=20, verbose_name='Fecha')),
                ('origen', models.CharField(max_length=20, verbose_name='Origen')),
                ('valor', models.IntegerField(verbose_name='Valor')),
                ('codigos', models.CharField(max_length=25, verbose_name='Codigos')),
                ('observacion', models.CharField(max_length=30, verbose_name='Observacion')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
