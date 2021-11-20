# Django
from django.db import models

# Utilities
from utils.models import LlegadaModel


DOCUMENTO_CHOICES = (
    ('DNI', 'DNI'),
    ('CUIL/CUIT', 'CUIL/CUIT'),
    ('PASAPORTE', 'PASAPORTE')
)


class Cliente(LlegadaModel):
    """Modelo de cliente."""

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    tipo_documento = models.CharField(choices=DOCUMENTO_CHOICES, max_length=10)
    numero_documento = models.CharField(max_length=20)
    telefono = models.IntegerField('Teléfono',)
    email = models.EmailField()
    localidad = models.CharField(max_length=100)
    puntos = models.IntegerField(default=0)

    def __str__(self):
        """Return nombre y apellido."""
        return f'{self.nombre} {self.apellido}'
