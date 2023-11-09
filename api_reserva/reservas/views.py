from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from .models import Reserva, Cliente, Encargado, Complejo, Cabania, Servicio, ReservaServicio
from .forms import formCabania, formEncargado, formCliente, formComplejo, formServicio, formReserva
from django.views.generic import  CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.views import LoginView
from datetime import date
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin 

# Create your views here.

def main(request):
    reservas = Reserva.objects.all()
    clientes = Cliente.objects.all()
    encargados = Encargado.objects.all()
    complejos = Complejo.objects.all()
    cabanias = Cabania.objects.all()
    servicios = Servicio.objects.all()
    reservaServicio = ReservaServicio.objects.all()

    context = {'reservas': reservas,
               'clientes': clientes,
               'encargados': encargados,
               'complejos': complejos,
               'cabanias': cabanias,
               'servicios':servicios,
               'reservaServicio':reservaServicio}
    
    return render(request, 'main.html', context)

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

#VISTAS ENCARGADO

class lista_encargados(LoginRequiredMixin,ListView):
    login_url = "/login/"
    model = Encargado
    template_name = 'lista_encargados.html'
    context_object_name = 'encargados'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q','')
        encargados = Encargado.objects.filter(
            Q(apellido_nombre__icontains=query) |
            Q(dni__icontains=query)
        )
        return encargados

class nuevo_encargado(LoginRequiredMixin,CreateView):
    login_url = "/login/"
    model = Encargado
    form_class = formEncargado
    template_name = 'form_encargado.html'
    success_url = reverse_lazy('lista_encargados')

class modif_encargado(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = Encargado
    form_class = formEncargado
    template_name = 'form_encargado.html'
    success_url = reverse_lazy('lista_encargados')

class borrar_encargado(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    model = Encargado
    template_name = 'conf_borrar_encargado.html'
    success_url = reverse_lazy('lista_encargados')

#VISTAS DE CABAÑAS

class lista_cabanias(LoginRequiredMixin, ListView):
    login_url = "/login/"
    model = Cabania
    template_name = 'lista_cabanias.html'
    context_object_name = 'cabanias'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        cabanias = Cabania.objects.filter(
            Q(nombre__contains = query) |
            Q(tipo__icontains = query)
        )

        return cabanias

class nuevo_cabania(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    model = Cabania
    form_class = formCabania
    template_name = 'form_cabania.html'
    success_url = reverse_lazy('lista_cabanias')

class modif_cabania(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = Cabania
    form_class = formCabania
    template_name = 'form_cabania.html'
    success_url = reverse_lazy('lista_cabanias')

class borrar_cabania(LoginRequiredMixin, DeleteView):
    LoginRequiredMixin = "/login/"
    model = Cabania
    template_name = 'conf_borrar_cabania.html'
    success_url = reverse_lazy('lista_cabanias')
  
#VISTAS DE CLIENTES

class lista_clientes(LoginRequiredMixin, ListView):
    login_url = "/login/"
    model = Cliente
    template_name = 'lista_clientes.html'
    context_object_name = 'clientes'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        clientes = Cliente.objects.filter(
            Q(apellido_nombre__icontains=query)| # Búsqueda por nombre del cliente
            Q(dni__icontains=query) |
            Q(telefono__icontains=query)            # Búsqueda por DNI del cliente
        )

        return  clientes

class nuevo_cliente(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    model = Cliente
    form_class = formCliente
    template_name = 'form_cliente.html'
    success_url = reverse_lazy('lista_clientes')

class modif_cliente(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = Cliente
    form_class = formCliente
    template_name = 'form_complejo.html'
    success_url = reverse_lazy('lista_clientes')

class borrar_cliente(LoginRequiredMixin, DeleteView):
    login_url ="/login/"
    model = Cliente
    template_name = 'conf_borrar_cliente.html'
    success_url = reverse_lazy('lista_clientes')
  
#VISTAS DE COMPLEJO
class lista_complejos(LoginRequiredMixin, ListView):
    login_url = "/login/"
    model = Complejo
    template_name = 'lista_complejos.html'
    context_object_name = 'complejos'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        complejos = Complejo.objects.filter(
            Q(nombre__icontains=query) 
        )

        return complejos

class nuevo_complejo(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    model = Complejo
    form_class = formComplejo
    template_name = 'form_complejo.html'
    success_url = reverse_lazy('lista_complejos')

class modif_complejo(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = Complejo
    form_class = formComplejo
    template_name = 'form_complejo.html'
    success_url = reverse_lazy('lista_complejos')

class borrar_complejo(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    model = Complejo
    template_name = 'conf_borrar_complejo.html'
    success_url = reverse_lazy('lista_complejos')
    
#VISTAS DE SERVICIOS
class lista_servicios(LoginRequiredMixin, ListView):
    login_url = "/login/"
    model = Servicio
    template_name = 'lista_servicios.html'
    context_object_name = 'servicios'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        servicios = Servicio.objects.filter(
            Q(nombre__icontains=query) 
        )
        return servicios


class nuevo_servicio(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    model = Servicio
    form_class = formServicio
    template_name = 'form_servicio.html'
    success_url = reverse_lazy('lista_servicios')

class modif_servicio(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = Servicio
    form_class = formServicio
    template_name = 'form_servicio.html'
    success_url = reverse_lazy('lista_servicios')

class borrar_servicio(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    model = Servicio
    template_name = 'conf_borrar_servicio.html'
    success_url = reverse_lazy('lista_servicios')
    
#VISTAS DE RESERVAS
class lista_reservas(LoginRequiredMixin, ListView):
    login_url  = "/login/"
    model = Reserva
    template_name = 'lista_reservas.html'
    context_object_name = 'reservas'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        reservas = Reserva.objects.filter(
            Q(cliente__apellido_nombre__icontains=query) |  # Búsqueda por nombre del cliente
            Q(cliente__dni__icontains=query)             # Búsqueda por DNI del cliente
        )

        return reservas
class nuevo_reserva(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    model = Reserva
    form_class = formReserva
    template_name = 'form_reserva.html'
    success_url = reverse_lazy('lista_reservas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = formReserva.ReservaServicioFormset(self.request.POST)
        else:
            context['formset'] = formReserva.ReservaServicioFormset()

        return context

    
    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid() and form.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))
        
    def total(self):
        reserva = Reserva.objects.get(pk=id)
        cabania = reserva.cabania.precio
        entrada = reserva.diaEntrada
        salida = reserva.diaSalida

        cantidad_dias = (salida - entrada).days 

        total_cabania = cabania * 2

        context = {
            'reserva': reserva,
            'cabania': cabania,
            'cantidad_dias': cantidad_dias,
            'total_cabania': total_cabania
        }

        return context
        
    

class modif_reserva(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = Reserva
    form_class = formReserva
    template_name = 'form_reserva.html'
    success_url = reverse_lazy('lista_reservas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        
        total_context = self.total()
        context.update(total_context)

        if self.request.POST:
            context['formset'] = formReserva.ReservaServicioFormset(self.request.POST, instance=self.object)
        else:
            context['formset'] = formReserva.ReservaServicioFormset(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        if formset.is_valid() and form.is_valid():
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))
        
    def total(self):
        reserva = self.object
        cabania = reserva.cabania.precio

        entrada = reserva.diaEntrada #dia entrada
        salida = reserva.diaSalida  #dia salida

        cantidad_dias = (salida - entrada).days #calculo de la diferencia entre dia de entrada y salida

        total_cabania = cabania * cantidad_dias #calculo entre el precio de la cabaña y la cantidad de dias

        total_servicios = 0 #calculo sobre el total de servicios

        total_reserva = total_cabania + total_servicios #calculo sobre el total de la reserva

        context = {
            'reserva': reserva,
            'cabania': cabania,
            'cantidad_dias': cantidad_dias,
            'total_cabania': total_cabania,
            'total_servicios': total_servicios,
            'total_reserva': total_reserva,
        }

        return context

class borrar_reserva(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    model = Reserva
    template_name = 'conf_borrar_reserva.html'
    success_url = reverse_lazy('lista_reservas')


class DetalleReservaServicio(LoginRequiredMixin, ListView):
    login_url = "/login/"
    model = ReservaServicio
    template_name = 'servicios-reserva.html'
    context_object_name = 'reservaservicio'

    def get_queryset(self):
        reserva_id = self.kwargs['reserva_id']  # Asumiendo que utilizas 'reserva_id' en la URL
        # Filtrar los objetos ReservaServicio relacionados con la reserva específica
        queryset = ReservaServicio.objects.filter(reserva_id=reserva_id)
        return queryset 
    
    
def Logout(request):
    logout(request)
    return redirect('/')

