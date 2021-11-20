# Django
from django.urls import path

# Views
from productos import views


urlpatterns = [
    path(
        route='',
        view=views.ProductsHomeView.as_view(),
        name='home'
    ),

    # ------------- PRODUCTOS -------------
    path(
        route='productos/',
        view=views.ProductsListView.as_view(),
        name='list_products'
    ),

    path(
        route='productos/delete/<int:pk>/',
        view=views.DeleteProductView.as_view(),
        name='delete'
    ),

    path(
        route='productos/create/',
        view=views.CreateProductView.as_view(),
        name='create'
    ),

    path(
        route='productos/editar/<int:pk>/',
        view=views.UpdateProductView.as_view(),
        name='update'
    ),

    path(
        route='productos/<int:pk>/',
        view=views.ListVentasPorProductoView.as_view(),
        name='list_producto'
    ),

    # ------------- TIPOS DE PRODUCTOS -------------
    path(
        route='tipos_productos/',
        view=views.KindProductListView.as_view(),
        name='list_kind'
    ),

    path(
        route='tipos_productos/create/',
        view=views.CreateKindView.as_view(),
        name='create_kind'
    ),

    path(
        route='tipos_productos/delete/<int:pk>/',
        view=views.DeleteKindView.as_view(),
        name='delete_kind'
    ),

    path(
        route='tipos_productos/editar/<int:pk>/',
        view=views.UpdateKindView.as_view(),
        name='update_kind'
    ),

]