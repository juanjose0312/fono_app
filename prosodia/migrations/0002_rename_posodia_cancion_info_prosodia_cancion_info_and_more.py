# Generated by Django 5.0.6 on 2024-08-16 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prosodia', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posodia_cancion_info',
            new_name='Prosodia_cancion_info',
        ),
        migrations.RenameModel(
            old_name='posodia_trabalenguas_info',
            new_name='Prosodia_trabalenguas_info',
        ),
    ]
