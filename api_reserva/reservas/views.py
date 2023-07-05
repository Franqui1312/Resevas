from django.shortcuts import render
from .models import Reserva, Cliente, Encargado, Complejo, Cabania, Servicio

# Create your views here.

def main(request):
    reservas = Reserva.objects.all()
    clientes = Cliente.objects.all()
    encargados = Encargado.objects.all()
    complejos = Complejo.objects.all()
    cabanias = Cabania.objects.all()
    servicios = Servicio.objects.all()

    context = {'reservas': reservas,
               'clientes': clientes,
               'encargados': encargados,
               'complejos': complejos,
               'cabanias': cabanias,
               'servicios':servicios}
    
    return render(request, 'main.html', context)

def tabla_reservas(request):
    reservas = Reserva.objects.all()

    context = {'reservas': reservas}
    return render(request, 'reservas.html', context)

def tabla_clientes(request):
    clientes = Cliente.objects.all()

    context = {'clientes': clientes}
    return render(request, 'clientes.html', context)

def tabla_encargados(request):
    encargados = Encargado.objects.all()

    context = {'encargados': encargados}
    return render(request, 'encargados.html', context)

def tabla_complejos(request):
    complejos = Complejo.objects.all()

    context = {'complejos': complejos}
    return render(request, 'complejos.html', context)

def tabla_cabanias(request):
    cabanias = Cabania.objects.all()

    context = {'cabanias': cabanias}
    return render(request, 'cabanias.html', context)

def tabla_servicios(request):
    servicios = Servicio.objects.all()

    context = {'servicios': servicios}
    return render(request, 'servicios.html', context)

def detalle_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id) #solo toma el id del cliente         #toma todos los atributos del cliente

    context = {
        'cliente': cliente
    }
    return render(request, 'detalle_cliente.html', context)

def detalle_encargado(request, encargado_id):
    encargado = Encargado.objects.get(id=encargado_id)

    context={
        'encargado': encargado
    }
    return render(request,'detalle_encargado.html', context)

def detalle_complejo(request, complejo_id):
    complejo = Complejo.objects.get(id=complejo_id)

    context = {
        'complejo': complejo
    }
    return render(request, 'detalle_complejo.html', context)

def detalle_cabania(request, cabania_id):
    cabania = Cabania.objects.get(id=cabania_id)

    context = {
        'cabania': cabania
    }
    return render(request, 'detalle_cabania.html', context)

def detalle_reserva(request, reserva_id):
    reserva = Reserva.objects.get(id=reserva_id)

    context = {
        'reserva': reserva
    }
    return render(request, 'detalle_reserva.html', context)

def detalle_servicio(request, servicio_id):
    servicio = Servicio.objects.get(id=servicio_id)

    context = {
        'servicio': servicio
    } 
    return render(request, 'detalle_servicio.html', context)