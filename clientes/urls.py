# Django
from django.urls import path

# Views
from clientes import views


urlpatterns = [
    path(
        route='',
        view=views.ListClientesView.as_view(),
        name='list'
    ),

    path(
        route='eliminar/<int:pk>/',
        view=views.DeleteClienteView.as_view(),
        name='delete'
    ),

    path(
        route='create/',
        view=views.CreateClienteView.as_view(),
        name='create'
    ),

    path(
        route='editar/<int:pk>/',
        view=views.UpdateClienteView.as_view(),
        name='update'
    ),

    path(
        route='<int:pk>/',
        view=views.ListVentasPorClienteView.as_view(),
        name='list-por-cliente'
    ),

    path(
        route='buscar/',
        view=views.buscarCliente,
        name='buscar'
    )
]