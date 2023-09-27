from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Reserva, Cliente, Encargado, Complejo, Cabania, Servicio
from .forms import formCabania, formEncargado, formCliente, formComplejo, formServicio, formReserva
from django.views.generic import  CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy

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

'''
def tabla_reservas(request):
    reservas = Reserva.objects.all()

    context = {'reservas': reservas}
    return render(request, 'reservas.html', context)
'''
def tabla_clientes(request):
    clientes = Cliente.objects.all()

    context = {'clientes': clientes}
    return render(request, 'clientes.html', context)

def tabla_encargados(request):
    encargados = Encargado.objects.all()

    context = {'encargados': encargados}
    return render(request, 'encargados.html', context)

def tabla_cabanias(request):
    cabanias = Cabania.objects.all()

    context = {'cabanias': cabanias}
    return render(request, 'cabanias.html', context)

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

#abm encargado

def modif_encargado(request, pk):
    encargado = Encargado.objects.get(id=pk)
    if request.method=='POST':
        form = formEncargado(request.POST, instance=encargado)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tabla_encargados'))
        
    else:
        form = formEncargado(instance=encargado)

    return render(request, 'form_encargado.html', {'form': form,'encargado': encargado})

def nuevo_encargado(request):
    if request.method=='POST':
        form = formEncargado(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tabla_encargados'))
        
    else:
        form = formEncargado()
    
    return render(request, 'form_encargado.html', {'form': form})

def borrar_encargado(request, pk):
    encargado = Encargado.objects.get(id=pk)
    if request.method=='POST':
        encargado.delete()
        return HttpResponseRedirect(reverse('tabla_encargados'))
    return render(request, 'conf_borrar_encargado.html', {'encargado': encargado})

#abm cabañas
def modif_cabania(request, pk):
    cabania = Cabania.objects.get(id=pk)
    if request.method=='POST':
        form = formCabania(request.POST, instance=cabania)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tabla_cabanias'))
        
    else:
        form = formCabania(instance=cabania)

    return render(request, 'form_cabania.html', {'form': form,'cabania': cabania})

def nuevo_cabania(request):
    if request.method=='POST':
        form = formCabania(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tabla_cabanias'))
        
    else:
        form = formCabania()
    
    return render(request, 'form_cabania.html', {'form': form})

def borrar_cabania(request, pk):
    cabania = Cabania.objects.get(id=pk)
    if request.method=='POST':
        cabania.delete()
        return HttpResponseRedirect(reverse('tabla_cabanias'))
    return render(request, 'conf_borrar_cabania.html', {'cabania': cabania})

#abm cliente
def modif_cliente(request, pk):
    cliente = Cliente.objects.get(id=pk)
    if request.method=='POST':
        form = formCliente(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tabla_clientes'))
        
    else:
        form = formCliente(instance=cliente)

    return render(request, 'form_cliente.html', {'form': form,'cliente': cliente})

def nuevo_cliente(request):
    if request.method=='POST':
        form = formCliente(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tabla_clientes'))
        
    else:
        form = formCliente()
    
    return render(request, 'form_cliente.html', {'form': form})

def borrar_cliente(request, pk):
    cliente = Cliente.objects.get(id=pk)
    if request.method=='POST':
        cliente.delete()
        return HttpResponseRedirect(reverse('tabla_cliente'))
    return render(request, 'conf_borrar_cliente.html', {'cliente': cliente})

#abm complejo
class tabla_complejos(ListView):
    model = Complejo
    template_name = 'complejos.html'
    context_object_name = 'complejos'

class nuevo_complejo(CreateView):
    model = Complejo
    form_class = formServicio
    template_name = 'form_complejo.html'
    success_url = reverse_lazy('tabla_complejos')

class modif_complejo(UpdateView):
    model = Complejo
    form_class = formServicio
    template_name = 'form_complejo.html'
    success_url = reverse_lazy('tabla_complejos')

class borrar_complejo(DeleteView):
    model = Complejo
    template_name = 'conf_borrar_complejo.html'
    success_url = reverse_lazy('tabla_complejos')
    
#abm servicios
class tabla_servicios(ListView):
    model = Servicio
    template_name = 'servicios.html'
    context_object_name = 'servicios'

class nuevo_servicio(CreateView):
    model = Servicio
    form_class = formServicio
    template_name = 'form_servicio.html'
    success_url = reverse_lazy('tabla_servicios')

class modif_servicio(UpdateView):
    model = Servicio
    form_class = formServicio
    template_name = 'form_servicio.html'
    success_url = reverse_lazy('tabla_servicios')

class borrar_servicio(DeleteView):
    model = Servicio
    template_name = 'conf_borrar_servicio.html'
    success_url = reverse_lazy('tabla_servicios')
    
#abm reservas
class tabla_reservas(ListView):
    model = Reserva
    template_name = 'reservas.html'
    context_object_name = 'reservas'
class nuevo_reserva(CreateView):
    model = Reserva
    form_class = formReserva
    template_name = 'form_reserva.html'
    success_url = reverse_lazy('tabla_reservas')

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
    success_url = reverse_lazy('tabla_reservas')

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
    success_url = reverse_lazy('tabla_reservas')

def servicioReserva(request,reserva_id):
    reserva = Reserva.objects.get(id=reserva_id)
    servicios = reserva.servicios.all()
    total_servicios = sum(servicio.precio for servicio in servicios)

    context = {
        'reserva' : reserva,
        'total_servicios' : total_servicios
    }

    return render(request, 'servicios-reserva.html', context)
