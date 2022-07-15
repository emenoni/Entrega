# Generated by Django 4.0.5 on 2022-07-13 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
                ('año', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('max_jugadores', models.IntegerField()),
                ('min_edad', models.IntegerField()),
            ],
        ),
    ]
