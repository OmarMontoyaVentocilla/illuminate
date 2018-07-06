# Generated by Django 2.0.4 on 2018-07-05 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_thumb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idfb', models.IntegerField(null=True, unique=True)),
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
    ]
