# Django
from django.db import models
from django.core.validators import MinValueValidator

# Utilities
from utils.models import LlegadaModel



class KindOfProduct(LlegadaModel):
    """Modelo del tipo de producto."""

    nombre = models.CharField(max_length=100,)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        """Retornar el nombre."""
        return self.nombre

    class Meta:
        """Meta class."""
        verbose_name = 'Tipo de producto'
        verbose_name_plural = 'Tipos de productos'


class Product(LlegadaModel):
    """Modelo del producto."""

    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    cantidad = models.FloatField(validators=[MinValueValidator(0.0)])
    stock_minimo = models.IntegerField()
    stock_maximo = models.IntegerField()
    proveedor = models.CharField(max_length=100,)
    marca = models.CharField(max_length=100,)
    tamaño = models.CharField(blank=True, max_length=100)
    ubicacion = models.CharField(blank=True, max_length=150)
    tipo_producto = models.ForeignKey(
        KindOfProduct,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        """Retornar el nombre del producto."""
        return self.nombre

    class Meta:
        """Meta class."""
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
