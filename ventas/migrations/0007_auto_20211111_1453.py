# Generated by Django 3.2.9 on 2021-11-11 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0006_alter_venta_forma_pago'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormaPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=15)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='venta',
            name='forma_pago',
            field=models.ForeignKey(choices=[('Contado', 'Contado'), ('Código QR', 'Código QR'), ('Tarjeta', 'Tarjeta')], help_text='Contado 10% Descuento', max_length=10, on_delete=django.db.models.deletion.CASCADE, to='ventas.formapago'),
        ),
    ]
