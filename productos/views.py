# Django
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, TemplateView, DetailView

# Models
from productos.models import Product, KindOfProduct
from ventas.models import Venta

# Forms
from productos.forms import ProductForm, KindProductForm


class ProductsHomeView(TemplateView):
    """Products home view."""

    template_name = 'productos/home.html'


# PRODUCTOS ------------------------------------------------------

class ProductsListView(ListView):
    """Listar todos los productos."""

    template_name = 'productos/list_products.html'
    context_object_name = 'productos'
    model = Product


class DeleteProductView(DeleteView):
    """Eliminar product."""

    template_name = 'productos/delete.html'
    model = Product
    success_url = reverse_lazy('productos:list_products')


class CreateProductView(CreateView):
    """Registrar product."""

    template_name = 'productos/create.html'
    form_class = ProductForm
    success_url = reverse_lazy('productos:list_products')


class UpdateProductView(UpdateView):
    """Actualizar product."""

    template_name = 'productos/update.html'
    model = Product
    fields = ('nombre', 'precio', 'cantidad', 'stock_minimo', 'stock_maximo', 'proveedor', 'marca', 'tamaño', 'ubicacion', 'tipo_producto')
    success_url = reverse_lazy('productos:list_products')
    context_object_name = 'producto'


class ListVentasPorProductoView(DetailView):
    """Listar todas las ventas por cliente."""

    template_name = 'productos/list_ventas_producto.html'
    context_object_name = 'product'
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        """Retornar las ventas por producto."""
        context = super().get_context_data(**kwargs)
        producto = self.get_object()
        context['ventas'] = Venta.objects.filter(producto=producto).order_by('-created')
        return context


# TIPOS DE PRODUCTOS ------------------------------------------------------

class KindProductListView(ListView):
    """Listar todos los tipos de producto."""

    template_name = 'productos/list_kind.html'
    context_object_name = 'kind_product'
    model = KindOfProduct


class CreateKindView(CreateView):
    """Registrar tipo de producto."""

    template_name = 'productos/create_kind.html'
    form_class = KindProductForm
    success_url = reverse_lazy('productos:list_kind')


class DeleteKindView(DeleteView):
    """Eliminar tipo de producto."""

    template_name = 'productos/delete_kind.html'
    model = KindProductForm
    queryset = KindOfProduct.objects.all()
    success_url = reverse_lazy('productos:list_kind')


class UpdateKindView(UpdateView):
    """Actualizar tipo de producto."""

    template_name = 'productos/update_kind.html'
    model = KindOfProduct
    fields = ('nombre', 'descripcion')
    success_url = reverse_lazy('productos:list_kind')
    context_object_name = 'kind'
