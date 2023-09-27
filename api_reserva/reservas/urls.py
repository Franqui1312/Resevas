
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),

    path('encargados/', views.tabla_encargados, name='tabla_encargados'),
    path('encargados/<int:encargado_id>/', views.detalle_encargado, name='detalle_encargado'),
    path('encargados/encargadoNuevo/', views.nuevo_encargado, name='nuevo_encargado'),
    path('encargados/encargadoModif/<int:pk>/', views.modif_encargado, name='modif_encargado'),
    path('encargados/encargadoBorrar/<int:pk>/', views.borrar_encargado, name='borrar_encargado'),

    path('clientes/', views.tabla_clientes, name='tabla_clientes'),
    path('clientes/<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
    path('clientes/clienteNuevo/', views.nuevo_cliente, name='nuevo_cliente'),
    path('clientes/clienteModif/<int:pk>/', views.modif_cliente, name='modif_cliente'),
    path('clientes/clienteBorrar/<int:pk>/', views.borrar_cliente, name='borrar_cliente'),

    path('cabanias/', views.tabla_cabanias, name='tabla_cabanias'),
    path('cabanias/<int:cabania_id>/', views.detalle_cabania, name='detalle_cabania'),
    path('cabanias/cabaniaNuevo/', views.nuevo_cabania, name='nuevo_cabania'),
    path('cabanias/cabaniaModif/<int:pk>/', views.modif_cabania, name='modif_cabania'),
    path('cabanias/cabaniaBorrar/<int:pk>/', views.borrar_cabania, name='borrar_cabania'),

    path('complejos/', views.tabla_complejos.as_view(), name='tabla_complejos'),
    path('complejos/<int:complejo_id>/', views.detalle_complejo, name='detalle_complejo'),
    path('complejos/complejoNuevo/', views.nuevo_complejo.as_view(), name='nuevo_complejo'),
    path('complejos/complejoModif/<int:pk>/', views.modif_complejo.as_view(), name='modif_complejo'),
    path('complejos/complejoBorrar/<int:pk>/', views.borrar_complejo.as_view(), name='borrar_complejo'),

    path('servicios/', views.tabla_servicios.as_view(), name='tabla_servicios'),
    path('servicios/<int:servicio_id>/', views.detalle_servicio, name='detalle_servicio'),
    path('servicios/servicioNuevo/', views.nuevo_servicio.as_view(), name='nuevo_servicio'),
    path('servicios/servicioModif/<int:pk>/', views.modif_servicio.as_view(), name='modif_servicio'),
    path('servicios/servicioBorrar/<int:pk>/', views.borrar_servicio.as_view(), name='borrar_servicio'),

    path('reservas/', views.tabla_reservas.as_view(), name='tabla_reservas'),
    path('reservas/<int:reserva_id>/', views.detalle_reserva, name='detalle_reserva'),
    path('reservas/reservaNuevo/', views.nuevo_reserva.as_view(), name='nuevo_reserva'),
    path('reservas/reservaModif/<int:pk>/', views.modif_reserva.as_view(), name='modif_reserva'),
    path('reservas/reservaBorrar/<int:pk>/', views.borrar_reserva.as_view(), name='borrar_reserva'),

    path('reservas/reserva/serviciosReserva/<int:reserva_id>/', views.servicioReserva, name='serviciosReserva')
]
