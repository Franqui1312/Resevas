
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

    path('encargados/encargadoNuevo/', views.nuevo_encargado, name='nuevo_encargado'),
    path('encargados/encargadoModif/<int:pk>/', views.modif_encargado, name='modif_encargado'),
    path('encargados/encargadoBorrar/<int:pk>/', views.borrar_encargado, name='borrar_encargado'),

    path('clientes/clienteNuevo/', views.nuevo_cliente, name='nuevo_cliente'),
    path('clientes/clienteModif/<int:pk>/', views.modif_cliente, name='modif_cliente'),
<<<<<<< HEAD
    path('clientes/clienteBorrar/<int:pk>/', views.borrar_cliente, name='borrar_cliente'),
=======
>>>>>>> 49f73bc3c3687db73288632ede484512c8d311bc

    path('cabanias/cabaniaNuevo/', views.nuevo_cabania, name='nuevo_cabania'),
    path('cabanias/cabaniaModif/<int:pk>/', views.modif_cabania, name='modif_cabania'),
    path('cabanias/cabaniaBorrar/<int:pk>/', views.borrar_cabania, name='borrar_cabania'),

<<<<<<< HEAD
    path('complejos/complejoNuevo/', views.nuevo_complejo, name='nuevo_complejo'),
    path('complejos/complejoModif/<int:pk>/', views.modif_complejo, name='modif_complejo'),
    path('complejos/complejoBorrar/<int:pk>/', views.borrar_complejo, name='borrar_complejo'),

    path('servicios/servicioNuevo/', views.nuevo_servicio, name='nuevo_servicio'),
    path('servicios/servicioModif/<int:pk>/', views.modif_servicio, name='modif_servicio'),
    path('servicios/servicioBorrar/<int:pk>/', views.borrar_servicio, name='borrar_servicio'),

    path('reservas/reservaNuevo/', views.nuevo_reserva, name='nuevo_reserva'),
    path('reservas/reservaModif/<int:pk>/', views.modif_reserva, name='modif_reserva'),
    path('reservas/reservaBorrar/<int:pk>/', views.borrar_reserva, name='borrar_reserva'),
=======
>>>>>>> 49f73bc3c3687db73288632ede484512c8d311bc
]
