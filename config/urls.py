# Django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Views
from config.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', view=HomeView.as_view(), name='home'),

    path('productos/', include(('productos.urls', 'productos'), namespace='productos')),
    path('clientes/', include(('clientes.urls', 'clientes'), namespace='clientes')),
    path('ventas/', include(('ventas.urls', 'ventas'), namespace='ventas')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
