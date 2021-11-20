# Django
from django import forms

# Models
from productos.models import Product, KindOfProduct


class ProductForm(forms.ModelForm):
    """Form model de producto."""

    class Meta:
        """Meta class."""
        model = Product
        fields = ('nombre', 'precio', 'cantidad', 'stock_minimo', 'stock_maximo', 'proveedor', 'marca', 'tamaño', 'ubicacion', 'tipo_producto')


class KindProductForm(forms.ModelForm):
    """Form model del tipo de producto."""

    class Meta:
        """Meta class."""
        model = KindOfProduct
        fields = ('nombre', 'descripcion')