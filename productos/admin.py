# Django
from django.contrib import admin

# Models
from productos.models import Product, KindOfProduct


admin.site.register(Product)
admin.site.register(KindOfProduct)