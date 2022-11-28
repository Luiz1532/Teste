# Generated by Django 4.1.3 on 2022-11-28 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250, verbose_name='Nome da pessoa')),
                ('email', models.CharField(max_length=250, verbose_name='E-mail')),
                ('celular', models.CharField(max_length=250, verbose_name='Número de celular')),
                ('tipo', models.IntegerField(choices=[(1, 'Administrador'), (2, 'Consumidor')], verbose_name='Tipo')),
            ],
        ),
    ]
