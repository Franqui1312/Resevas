
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('reservas/', views.tabla_reservas, name='tabla_reservas'),
    path('clientes/', views.tabla_clientes, name='tabla_clientes'),
    path('encargados/', views.tabla_encargados, name='tabla_encargados'),
    path('complejos/', views.tabla_complejos, name='tabla_complejos'),
    path('cabanias/', views.tabla_cabanias, name='tabla_cabanias'),
    path('servicios/', views.tabla_servicios, name='tabla_servicios'),
    path('clientes/<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
    path('encargados/<int:encargado_id>/', views.detalle_encargado, name='detalle_encargado'),
    path('complejos/<int:complejo_id>/', views.detalle_complejo, name='detalle_complejo'),
    path('cabanias/<int:cabania_id>/', views.detalle_cabania, name='detalle_cabania'),
    path('reservas/<int:reserva_id>/', views.detalle_reserva, name='detalle_reserva'),
    path('servicios/<int:servicio_id>/', views.detalle_servicio, name='detalle_servicio'),
]
