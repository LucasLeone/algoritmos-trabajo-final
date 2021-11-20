# Django
from django.db import models
from django.core.validators import MinValueValidator

# Models
from clientes.models import Cliente
from productos.models import Product

# Utilities
from utils.models import LlegadaModel
from django.utils import timezone


PAGO_CHOICES = (
    ('Contado', 'Contado'),
    ('Código QR','Código QR'),
    ('Tarjeta','Tarjeta') 
)


class FormaPago(LlegadaModel):
    """Modelo de Forma de pago."""

    nombre = models.CharField(max_length=15)

    def __str__(self):
        """Retornar el nombre de la forma de pago."""
        return self.nombre


class Venta(LlegadaModel):
    """Modelo de venta."""

    fecha = models.DateTimeField(default=timezone.now, help_text='Ejemplo: 09/11/2021 17:20:00')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    cantidad = models.FloatField(validators=[MinValueValidator(0.0)])
    forma_pago = models.ForeignKey(FormaPago, max_length=10, help_text='Contado 10% Descuento', on_delete=models.CASCADE)

    def __str__(self):
        """Return id, date and client."""
        return f'{self.pk} - {self.fecha} - {self.cliente}'

    def subtotal(self):
        """Obtener el subtotal"""
        total = self.producto.precio * self.cantidad
        total = round(total, 2)
        return total

    def descuento(self):
        """Obtener el descuento."""
        total = self.producto.precio * self.cantidad
        descuento = round(total, 2)
        if self.forma_pago.nombre == 'Contado':
            descuento = (descuento * 0.1)
            descuento = round(descuento, 2)
            return descuento
        else:
            return 0

    def get_total(self):
        """Obtener el total de la venta."""
        total = self.producto.precio * self.cantidad
        total_round = round(total, 3)
        if self.forma_pago.nombre == 'Contado':
            total_round = total_round - (total_round * 0.1 )
        return total_round

    