# Generated by Django 5.1 on 2024-10-03 02:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discriminacion_auditiva', '0002_discriminacion_auditiva_escoger_info_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seleccion', models.CharField(max_length=100)),
                ('es_correcta', models.BooleanField(default=False)),
                ('instruccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discriminacion_auditiva.discriminacion_auditiva_escoger_info')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
