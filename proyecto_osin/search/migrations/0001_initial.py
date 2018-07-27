# Generated by Django 2.0.4 on 2018-07-27 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persona', '0002_auto_20180525_1903'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=8, unique=True)),
                ('nombres', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('descripcion_vida', models.TextField()),
                ('edad', models.IntegerField()),
                ('tiempo_registro', models.DateTimeField(auto_now=True)),
                ('cantidad_dinero', models.DecimalField(decimal_places=2, max_digits=5)),
                ('thumb', models.ImageField(blank=True, default='default.png', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Facebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idfb', models.CharField(max_length=17, null=True, unique=True)),
                ('nombres', models.CharField(max_length=100)),
                ('biografia', models.TextField()),
                ('foto', models.TextField()),
                ('url', models.TextField()),
                ('trabajo', models.CharField(max_length=300)),
                ('lugar', models.CharField(max_length=300)),
                ('estudio', models.CharField(max_length=300)),
                ('estado', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Github',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biografia_github', models.TextField()),
                ('email_github', models.CharField(max_length=100)),
                ('img_github', models.CharField(max_length=250)),
                ('nick_github', models.CharField(max_length=100)),
                ('nombre_github', models.CharField(max_length=150)),
                ('pagina_github', models.TextField()),
                ('pais_github', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Google',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_google', models.CharField(max_length=150)),
                ('url_google', models.TextField()),
                ('img_google', models.TextField()),
                ('info_google', models.TextField()),
                ('estado', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Instagram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_instagram', models.TextField()),
                ('usuario_instagram', models.CharField(max_length=150)),
                ('url_instagram', models.CharField(max_length=250)),
                ('foto_instagram', models.CharField(max_length=280)),
                ('seguidores_instagram', models.CharField(max_length=150)),
                ('post_instagram', models.CharField(max_length=150)),
                ('siguiendo_instagram', models.CharField(max_length=150)),
                ('estado', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='PersonaRedes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=2)),
                ('idfb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facebookdata', to='search.Facebook')),
                ('idgoogle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='googledata', to='search.Google')),
                ('idinstagram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instagramdata', to='search.Instagram')),
                ('idpersona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personadata', to='persona.Persona')),
            ],
        ),
        migrations.CreateModel(
            name='Twitter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio_tw', models.CharField(max_length=100)),
                ('cant_tw', models.CharField(max_length=50)),
                ('url', models.TextField()),
                ('img_tw', models.TextField()),
                ('nombre_tw', models.CharField(max_length=50)),
                ('nombre_cuenta_tw', models.CharField(max_length=150)),
                ('pagina_web', models.TextField()),
                ('biografia', models.TextField()),
                ('seguidores', models.CharField(max_length=50)),
                ('siguiendo', models.CharField(max_length=50)),
                ('tweets', models.CharField(max_length=50)),
                ('ubicacion', models.CharField(max_length=50)),
                ('likes', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='personaredes',
            name='idtw',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='twitterdata', to='search.Twitter'),
        ),
        migrations.AddField(
            model_name='personaredes',
            name='idusuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuariodata', to=settings.AUTH_USER_MODEL),
        ),
    ]
