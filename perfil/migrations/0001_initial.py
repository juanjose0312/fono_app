# Generated by Django 5.0.6 on 2024-09-18 19:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='perfil_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_de_idetificacion', models.TextField(max_length=100, verbose_name='Número de identificación')),
                ('nombre', models.TextField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.TextField(max_length=100, verbose_name='Apellido')),
                ('email', models.TextField(max_length=100, verbose_name='Email')),
                ('fecha_de_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('genero', models.TextField(max_length=100, verbose_name='Género')),
                ('escolaridad', models.TextField(max_length=100, verbose_name='Escolaridad')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='nombre de usuario')),
            ],
        ),
    ]
