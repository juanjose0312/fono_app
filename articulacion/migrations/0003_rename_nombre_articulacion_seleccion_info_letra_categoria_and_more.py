# Generated by Django 5.1 on 2024-08-19 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulacion', '0002_remove_articulacion_completar_info_nombre_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulacion_seleccion_info',
            old_name='nombre',
            new_name='letra_categoria',
        ),
        migrations.AlterField(
            model_name='articulacion_completar_info',
            name='letra_categoria',
            field=models.TextField(max_length=100, verbose_name='letra'),
        ),
    ]
