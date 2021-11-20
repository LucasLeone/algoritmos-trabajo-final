# Django
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

# Models
from ventas.models import Venta
from clientes.models import Cliente

# Forms
from clientes.forms import ClienteForm


class ListClientesView(ListView):
    """Listar todos los clientes."""

    template_name = 'clientes/list_clientes.html'
    context_object_name = 'clientes'
    model = Cliente


class DeleteClienteView(DeleteView):
    """Eliminar cliente."""

    template_name = 'clientes/delete.html'
    model = Cliente
    success_url = reverse_lazy('clientes:list')
    context_object_name = 'cliente'


class CreateClienteView(CreateView):
    """Registrar cliente."""

    template_name = 'clientes/create.html'
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:list')


class UpdateClienteView(UpdateView):
    """Actualizar cliente."""

    template_name = 'clientes/update.html'
    model = Cliente
    fields = ('nombre', 'apellido', 'tipo_documento', 'numero_documento', 'telefono', 'email', 'localidad', 'puntos')
    success_url = reverse_lazy('clientes:list')
    context_object_name = 'cliente'


class ListVentasPorClienteView(DetailView):
    """Listar todas las ventas por cliente."""

    template_name = 'clientes/list_ventas_cliente.html'
    context_object_name = 'cliente'
    queryset = Cliente.objects.all()

    def get_context_data(self, **kwargs):
        """Return sales by costumer."""
        context = super().get_context_data(**kwargs)
        cliente = self.get_object()
        context['ventas'] = Venta.objects.filter(cliente=cliente).order_by('-created')
        return context


def buscarCliente(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            (Q(nombre__icontains=query)) |
            (Q(numero_documento__icontains=query))
        )
        results = Cliente.objects.filter(qset)
    else:
        results = []
    return render(None, 'clientes/search.html', {
        "results": results,
        "query": query,
    })