# Django
from django import forms

from clientes.models import Cliente

# Models
from .models import Venta
from productos.models import Product

from django.utils.timezone import now


class DateInput(forms.DateInput):
    input_type = 'datetime-local'


class VentasForm(forms.ModelForm):
    """Formulario modelo de ventas."""

    # fecha = forms.DateField(widget=DateInput({'step': 1}), help_text='<small>La hora por defecto es la actual</small>')

    class Meta:
        """Meta class."""
        model = Venta
        fields = ('fecha', 'cliente', 'producto', 'cantidad', 'forma_pago')

    def clean(self):
        """Verificar si hay stock del producto."""
        data = super().clean()

        producto = Product.objects.get(id=data['producto'].pk)
        
        if producto.cantidad < float(data['cantidad']):
            raise forms.ValidationError('No hay suficiente stock del producto.')

        if float(data['cantidad']) == 0:
            raise forms.ValidationError('Cantidad invalida.')

        return data

    def save(self):
        """Restar stock."""
        data = self.cleaned_data

        producto = Product.objects.get(id=data['producto'].pk)
        cliente = Cliente.objects.get(id=data['cliente'].pk)

        producto.cantidad -= float(data['cantidad'])
        producto.save()

        cliente.puntos += int((data['cantidad'] * producto.precio) / 10)
        cliente.save()

        return super().save()