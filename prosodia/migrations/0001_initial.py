# Generated by Django 5.1 on 2024-08-11 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posodia_cancion_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=100, verbose_name='nombre')),
                ('parrafo_1', models.TextField(max_length=1000, verbose_name='parrafo_1')),
                ('respuesta_1', models.TextField(max_length=100, verbose_name='respuesta_1')),
                ('parrafo_2', models.TextField(max_length=1000, verbose_name='parrafo_2')),
                ('respuesta_2', models.TextField(max_length=100, verbose_name='respuesta_2')),
                ('parrafo_3', models.TextField(max_length=1000, verbose_name='parrafo_3')),
                ('respuesta_3', models.TextField(max_length=100, verbose_name='respuesta_3')),
                ('parrafo_4', models.TextField(max_length=1000, verbose_name='parrafo_4')),
                ('respuesta_4', models.TextField(max_length=100, verbose_name='respuesta_4')),
                ('parrafo_5', models.TextField(max_length=1000, verbose_name='parrafo_5')),
                ('respuesta_5', models.TextField(max_length=100, verbose_name='respuesta_5')),
            ],
        ),
        migrations.CreateModel(
            name='posodia_trabalenguas_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=100, verbose_name='nombre')),
                ('imagen', models.ImageField(upload_to='fotos/', verbose_name='imagen')),
                ('transcripcion_trabalenguas', models.TextField(max_length=300, verbose_name='transcripcion')),
            ],
        ),
    ]
