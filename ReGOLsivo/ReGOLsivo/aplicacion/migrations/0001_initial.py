# Generated by Django 3.0.6 on 2020-05-18 11:59

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nombre', models.CharField(max_length=35)),
                ('apellidos', models.CharField(max_length=35)),
                ('nombreDeUsuario', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensajeBienvenida', models.TextField(max_length=60)),
                ('linkLogo', models.URLField()),
                ('valorComentariosPositivos', models.PositiveIntegerField(default=50)),
                ('premioComentariosPositivos', models.PositiveIntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreLocal', models.CharField(max_length=35)),
                ('nombreVisitante', models.CharField(max_length=35)),
                ('resultado', models.CharField(max_length=35)),
                ('hora', models.TimeField()),
                ('dia', models.DateField()),
                ('pronosticoSistema', models.CharField(max_length=35)),
                ('premio', models.PositiveIntegerField()),
                ('dificultad', models.CharField(choices=[('Fácil', 'Facil'), ('Intermedia', 'Intermedia'), ('Difícil', 'Dificil')], max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('actor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aplicacion.Actor')),
                ('email', models.EmailField(max_length=35)),
            ],
            options={
                'abstract': False,
            },
            bases=('aplicacion.actor',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('actor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aplicacion.Actor')),
                ('email', models.EmailField(max_length=35)),
                ('karma', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=('aplicacion.actor',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Pronostico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultado', models.CharField(max_length=35)),
                ('acertado', models.BooleanField(default=False)),
                ('partido', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Partido')),
                ('usuario', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('momento', models.DateTimeField(auto_now_add=True)),
                ('texto', models.TextField()),
                ('meGustas', models.PositiveIntegerField(default=0)),
                ('comentarioRespuesta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Comentario')),
                ('partido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Partido')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Usuario')),
            ],
        ),
    ]
