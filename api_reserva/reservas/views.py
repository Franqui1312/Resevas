from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Reserva, Cliente, Encargado, Complejo, Cabania, Servicio, ReservaServicio
from .forms import formCabania, formEncargado, formCliente, formComplejo, formServicio, formReserva
from django.views.generic import  CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.db.models import Q

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

class lista_encargados(ListView):
    model = Encargado
    template_name = 'lista_encargados.html'
    context_object_name = 'encargados'

class nuevo_encargado(CreateView):
    model = Encargado
    form_class = formEncargado
    template_name = 'form_encargado.html'
    success_url = reverse_lazy('lista_encargados')

class modif_encargado(UpdateView):
    model = Encargado
    form_class = formEncargado
    template_name = 'form_encargado.html'
    success_url = reverse_lazy('lista_encargados')

class borrar_encargado(DeleteView):
    model = Encargado
    template_name = 'conf_borrar_encargado.html'
    success_url = reverse_lazy('lista_encargados')

#VISTAS DE CABAÑAS

class lista_cabanias(ListView):
    model = Cabania
    template_name = 'lista_cabanias.html'
    context_object_name = 'cabanias'

class nuevo_cabania(CreateView):
    model = Cabania
    form_class = formCabania
    template_name = 'form_cabania.html'
    success_url = reverse_lazy('lista_cabanias')

class modif_cabania(UpdateView):
    model = Cabania
    form_class = formCabania
    template_name = 'form_cabania.html'
    success_url = reverse_lazy('lista_cabanias')

class borrar_cabania(DeleteView):
    model = Cabania
    template_name = 'conf_borrar_cabania.html'
    success_url = reverse_lazy('lista_cabanias')
  
#VISTAS DE CLIENTES

class lista_clientes(ListView):
    model = Cliente
    template_name = 'lista_clientes.html'
    context_object_name = 'clientes'

class nuevo_cliente(CreateView):
    model = Cliente
    form_class = formCliente
    template_name = 'form_cliente.html'
    success_url = reverse_lazy('lista_clientes')

class modif_cliente(UpdateView):
    model = Cliente
    form_class = formCliente
    template_name = 'form_complejo.html'
    success_url = reverse_lazy('lista_clientes')

class borrar_cliente(DeleteView):
    model = Cliente
    template_name = 'conf_borrar_cliente.html'
    success_url = reverse_lazy('lista_clientes')
  
#VISTAS DE COMPLEJO
class lista_complejos(ListView):
    model = Complejo
    template_name = 'lista_complejos.html'
    context_object_name = 'complejos'

class nuevo_complejo(CreateView):
    model = Complejo
    form_class = formComplejo
    template_name = 'form_complejo.html'
    success_url = reverse_lazy('lista_complejos')

class modif_complejo(UpdateView):
    model = Complejo
    form_class = formComplejo
    template_name = 'form_complejo.html'
    success_url = reverse_lazy('lista_complejos')

class borrar_complejo(DeleteView):
    model = Complejo
    template_name = 'conf_borrar_complejo.html'
    success_url = reverse_lazy('lista_complejos')
    
#VISTAS DE SERVICIOS
class lista_servicios(ListView):
    model = Servicio
    template_name = 'lista_servicios.html'
    context_object_name = 'servicios'

class nuevo_servicio(CreateView):
    model = Servicio
    form_class = formServicio
    template_name = 'form_servicio.html'
    success_url = reverse_lazy('lista_servicios')

class modif_servicio(UpdateView):
    model = Servicio
    form_class = formServicio
    template_name = 'form_servicio.html'
    success_url = reverse_lazy('lista_servicios')

class borrar_servicio(DeleteView):
    model = Servicio
    template_name = 'conf_borrar_servicio.html'
    success_url = reverse_lazy('lista_servicios')
    
#VISTAS DE RESERVAS
class lista_reservas(ListView):
    model = Reserva
    template_name = 'lista_reservas.html'
    context_object_name = 'reservas'

    def get(self, request):
        query = request.GET.get('q', '')
        reservas = Reserva.objects.filter(
            Q(cliente__apellido_nombre__icontains=query) |  # Búsqueda por nombre del cliente
            Q(cliente__dni__icontains=query)             # Búsqueda por DNI del cliente
        )

        context = {
            'reservas': reservas,
            'query': query
        }

        return render(request, self.template_name, context)
class nuevo_reserva(CreateView):
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

class modif_reserva(UpdateView):
    model = Reserva
    form_class = formReserva
    template_name = 'form_reserva.html'
    success_url = reverse_lazy('lista_reservas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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

class borrar_reserva(DeleteView):
    model = Reserva
    template_name = 'conf_borrar_reserva.html'
    success_url = reverse_lazy('lista_reservas')
'''
def servicioReserva(request, reserva_id):
    try:
        #reservaServicio = ReservaServicio.objects.get(id=reserva_id)
        #reserva = reservaServicio.reserva
        reserva = Reserva.objects.get(id=reserva_id)
        servicios = reserva.servicios.all()
        total_servicios = sum(servicio.precio for servicio in servicios)

        #print("Reserva Servicio:", reserva_servicio)
        print("Reserva:", reserva)
        print("Servicios:", servicios)
        print("Total Servicios:", total_servicios)

        context = {
            #'reserva_servicio': reserva_servicio,
            'reserva': reserva,
            'total_servicios': total_servicios,
        }

        return render(request, 'servicios-reserva.html', context)
    except ReservaServicio.DoesNotExist:
        # Maneja el caso en el que no se encuentre la ReservaServicio
        # Puedes redirigir a una página de error o realizar otra acción apropiada.
        return render(request, 'error.html', {'message': 'ReservaServicio no encontrada'})

def servicioReserva(request, reserva_id):
    context = {}  # Inicializa context vacío por defecto

    try:
        reserva_servicio = ReservaServicio.objects.get(id=reserva_id)
        servicio = reserva_servicio.objects.all()
        total_servicios = sum(servicio.precio for servicio in servicios)

        print("Reserva Servicio:", reserva_servicio)
        print("Servicio:", servicio)
        print("Total Servicios:", total_servicios)

        context = {
            'reserva_servicio': reserva_servicio,
            'total_servicios': total_servicios,
        }

    except ReservaServicio.DoesNotExist:
        context = {
            'alert': 'ReservaServicio no encontrada'
        }

    return render(request, 'servicios-reserva.html', context)
    '''

class DetalleReservaServicio(ListView):
    model = ReservaServicio
    template_name = 'servicios-reserva.html'
    context_object_name = 'reservaservicio'

    def get_queryset(self):
        reserva_id = self.kwargs['reserva_id']  # Asumiendo que utilizas 'reserva_id' en la URL
        # Filtrar los objetos ReservaServicio relacionados con la reserva específica
        queryset = ReservaServicio.objects.filter(reserva_id=reserva_id)
        return queryset 
