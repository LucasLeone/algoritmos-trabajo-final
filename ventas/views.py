# Django
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.detail import DetailView

# Models
from .models import FormaPago, Venta

# Forms
from .forms import VentasForm


class ListVentasView(ListView):
    """Listar todas las ventas."""

    template_name = 'ventas/list.html'
    context_object_name = 'ventas'
    model = Venta


class DeleteVentasView(DeleteView):
    """Borrar venta.."""

    template_name = 'ventas/delete.html'
    model = Venta
    success_url = reverse_lazy('ventas:list')
    context_object_name = 'venta'


class CreateVentasView(CreateView):
    """Registrar venta."""

    template_name = 'ventas/create.html'
    form_class = VentasForm
    context_object_name = 'venta'

    def get_success_url(self):
        ventaid = self.object.pk
        return reverse_lazy('ventas:ticket', kwargs={'pk': ventaid})


class UpdateVentasView(UpdateView):
    """Actualizar venta."""

    template_name = 'ventas/update.html'
    model = Venta
    form_class = VentasForm
    success_url = reverse_lazy('ventas:list')
    context_object_name = 'venta'


class ListVentasPorPagoView(DetailView):
    """Listar todas las ventas por forma de pago."""

    template_name = 'ventas/list_pago.html'
    context_object_name = 'ventas'
    queryset = FormaPago.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        forma_pago = self.get_object()
        context['ventas'] = Venta.objects.filter(forma_pago=forma_pago).order_by('-created')
        return context


class ListVentasPorFechaView(ListView):
    """Listar todas las ventas por rango de fecha. SOLO PROTOTIPO"""

    template_name = 'ventas/list_fecha.html'
    context_object_name = 'ventas'
    model = Venta


class TicketView(DetailView):
    """Ver el ticket de la venta."""

    template_name = 'ventas/ticket.html'
    context_object_name = 'venta'
    queryset = Venta.objects.all()