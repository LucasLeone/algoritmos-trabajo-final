# Generated by Django 3.2.9 on 2021-11-11 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0007_auto_20211111_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='forma_pago',
            field=models.CharField(choices=[('Contado', 'Contado'), ('Código QR', 'Código QR'), ('Tarjeta', 'Tarjeta')], help_text='Contado 10% Descuento', max_length=10),
        ),
        migrations.DeleteModel(
            name='FormaPago',
        ),
    ]
