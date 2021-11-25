# Django
from django.db import models


class LlegadaModel(models.Model):
    """Modelo base para todos los modelos de la app."""

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta option."""

        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']