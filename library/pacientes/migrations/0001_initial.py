# Generated by Django 3.2.12 on 2022-02-02 13:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id_paciente', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('idade', models.IntegerField()),
                ('cpf', models.CharField(max_length=255)),
                ('rg', models.CharField(max_length=255)),
                ('data_nasc', models.DateField()),
                ('sexo', models.CharField(max_length=255)),
                ('signo', models.CharField(max_length=255)),
                ('mae', models.CharField(max_length=255)),
                ('pai', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('senha', models.CharField(max_length=255)),
                ('cep', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
                ('telefone_fixo', models.CharField(max_length=255)),
                ('celular', models.CharField(max_length=255)),
                ('altura', models.CharField(max_length=255)),
                ('tipo_sanguineo', models.CharField(max_length=255)),
                ('cor', models.CharField(max_length=255)),
            ],
        ),
    ]