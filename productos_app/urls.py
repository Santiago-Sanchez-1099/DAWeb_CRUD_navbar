from django.urls import path
from  productos_app import views

urlpatterns = [
    path('producto', views.inicio_vistaProducto, name='producto'),
    path('registrarProducto/',views.registrarProducto,name='registrarProducto'),
    path('seleccionarProducto/<id_producto>', views.seleccionarProducto, name='seleccionarProducto'),
    path('editarProducto/',views.editarProducto,name='editarProducto'),
    path('borrarProducto/<id_producto>',views.borrarProducto,name='borrarProducto'),
]