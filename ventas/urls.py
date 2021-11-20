# Django
from django.urls import path

# Views
from . import views


urlpatterns = [
    path(
        route='',
        view=views.ListVentasView.as_view(),
        name='list'
    ),

    path(
        route='update/<int:pk>/',
        view=views.UpdateVentasView.as_view(),
        name='update'
    ),

    path(
        route='delete/<int:pk>/',
        view=views.DeleteVentasView.as_view(),
        name='delete'
    ),

    path(
        route='create/',
        view=views.CreateVentasView.as_view(),
        name='create'
    ),

    path(
        route='informes/<int:pk>/',
        view=views.ListVentasPorPagoView.as_view(),
        name='list-pago'
    ),

    path(
        route='informes/fecha/',
        view=views.ListVentasPorFechaView.as_view(),
        name='list-fecha'
    ),

    path(
        route='ticket/<int:pk>/',
        view=views.TicketView.as_view(),
        name='ticket'
    ),

]