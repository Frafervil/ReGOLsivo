# Generated by Django 3.0.6 on 2020-08-25 00:22

import computed_property.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0012_auto_20200825_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partido',
            name='pronosticoSistema',
            field=computed_property.fields.ComputedIntegerField(compute_from='calcular_pronostico', editable=False),
        ),
    ]