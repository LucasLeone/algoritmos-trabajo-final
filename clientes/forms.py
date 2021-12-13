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

    def clean(self):
        """Verificar los datos introducidos."""
        data = super().clean()

        if len(data['nombre']) < 2:
            raise forms.ValidationError('El nombre debe tener por lo menos 2 letras.')

        if len(data['apellido']) < 2:
            raise forms.ValidationError('El apellido debe tener por lo menos 2 letras.')

        if len(data['numero_documento']) < 4:
            raise forms.ValidationError('El DNI debe tener por lo menos 5 números.')
            
        if len(data['localidad']) < 3:
            raise forms.ValidationError('La localidad debe tener por lo menos 3 letras.')

        if len(data['telefono']) < 5:
            raise forms.ValidationError('El número de telefono debe tener por lo menos 5 números.')

        if data['puntos'] < 0:
            raise forms.ValidationError('Los puntos no pueden ser menor a 0.')

        return data

    def save(self):
        """Guardar cliente."""
        data = self.cleaned_data

        cliente = Cliente.objects.create(
            nombre=data['nombre'],
            apellido=data['apellido'],
            tipo_documento=data['tipo_documento'],
            numero_documento=data['numero_documento'],
            telefono=data['telefono'],
            email=data['email'],
            localidad=data['localidad'],
            puntos=data['puntos'],
        )

        cliente.save()

        return super().save()