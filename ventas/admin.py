# Django
from django.contrib import admin

# Models
from .models import Venta, FormaPago

admin.site.register(Venta)
admin.site.register(FormaPago)