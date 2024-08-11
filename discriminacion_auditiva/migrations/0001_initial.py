# Generated by Django 5.1 on 2024-08-11 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discriminacion_auditiva_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=100, verbose_name='nombre')),
                ('imagen', models.ImageField(upload_to='fotos/', verbose_name='imagen')),
                ('audio', models.FileField(upload_to='audios/', verbose_name='audio')),
            ],
        ),
    ]
