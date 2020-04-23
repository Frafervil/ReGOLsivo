# Generated by Django 3.0.5 on 2020-04-23 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='configuracion',
            old_name='mensajeBienvenidaEs',
            new_name='mensajeBienvenida',
        ),
        migrations.RemoveField(
            model_name='configuracion',
            name='mensajeBienvenidaIn',
        ),
        migrations.AddField(
            model_name='configuracion',
            name='premioComentariosPositivos',
            field=models.PositiveIntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Usuario'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='texto',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='valorComentariosPositivos',
            field=models.PositiveIntegerField(default=50),
        ),
    ]
