# Generated by Django 3.2.9 on 2021-11-16 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_alter_cliente_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='puntos',
            field=models.IntegerField(default=0),
        ),
    ]