# Generated by Django 3.0.6 on 2020-06-03 15:21

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
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
                ('actor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
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
                ('actor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('karma', models.IntegerField(default=20)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
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
            name='Logro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('usuarios', models.ManyToManyField(to='aplicacion.Usuario')),
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
