# Este es el archivo que modificas: ordenes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ordenes, name='lista_ordenes'),
    path('nueva/', views.crear_orden, name='crear_orden'),
    path('<int:orden_id>/', views.detalle_orden, name='detalle_orden'),
    path('<int:orden_id>/editar/', views.editar_orden, name='editar_orden'),
    path('<int:orden_id>/eliminar/', views.eliminar_orden, name='eliminar_orden'),
    path('<int:orden_id>/registrar-viaje/', views.registrar_viaje, name='registrar_viaje'),
]
