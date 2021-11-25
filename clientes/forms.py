# Django
from django import forms

# Models
from clientes.models import Cliente


class ClienteForm(forms.ModelForm):
    """Modelo del formulario de cliente."""

    class Meta:
        """Meta class."""
        model = Cliente
        fields = ('nombre', 'apellido', 'tipo_documento', 'numero_documento', 'telefono', 'email', 'localidad', 'puntos')
