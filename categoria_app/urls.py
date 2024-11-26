from django.urls import path
from  categoria_app import views

urlpatterns = [
    path('categoria', views.inicio_vistaCategoria, name='categoria'),
    path('registrarCategoria/',views.registrarCategoria,name='registrarCategoria'),
    path('seleccionarCategoria/<id_categoria>', views.seleccionarCategoria, name='seleccionarCategoria'),
    path('editarCategoria/',views.editarCategoria,name='editarCategoria'),
    path('borrarCategoria/<id_categoria>',views.borrarCategoria,name='borrarCategoria'),
]