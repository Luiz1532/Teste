# Generated by Django 4.1.3 on 2022-11-28 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Garagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=250, verbose_name='E-mail')),
                ('celular', models.CharField(max_length=250, verbose_name='Número de celular')),
            ],
        ),
    ]
