# Generated by Django 3.0.6 on 2020-08-24 23:26

import computed_property.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0011_auto_20200825_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partido',
            name='goles_por_partido_del_equipo_local',
            field=models.DecimalField(decimal_places=9, max_digits=11),
        ),
        migrations.AlterField(
            model_name='partido',
            name='goles_por_partido_del_equipo_visitante',
            field=models.DecimalField(decimal_places=9, max_digits=11),
        ),
        migrations.AlterField(
            model_name='partido',
            name='pronosticoSistema',
            field=computed_property.fields.ComputedDecimalField(compute_from='calcular_pronostico', decimal_places=9, editable=False, max_digits=11),
        ),
        migrations.AlterField(
            model_name='partido',
            name='proporcion_de_puntos_del_equipo_local',
            field=models.DecimalField(decimal_places=9, max_digits=11),
        ),
        migrations.AlterField(
            model_name='partido',
            name='proporcion_de_puntos_del_equipo_visitante',
            field=models.DecimalField(decimal_places=9, max_digits=11),
        ),
    ]
