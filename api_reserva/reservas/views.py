from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from .models import Reserva, Cliente, Encargado, Complejo, Cabania, Servicio, ReservaServicio
from .forms import formCabania, formEncargado, formCliente, formComplejo, formServicio, formReserva
from django.views.generic import  CreateView, UpdateView, DeleteView, ListView, View
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date, timedelta
from django.contrib.auth import logout
from django.http import HttpResponse

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


    cabania = reserva.cabania.precio

    entrada = reserva.diaEntrada #dia entrada
    salida = reserva.diaSalida  #dia salida

    cantidad_dias = (salida - entrada).days #calculo de la diferencia entre dia de entrada y salida

    total_cabania = cabania * cantidad_dias #calculo entre el precio de la cabaña y la cantidad de dias

    total_servicios = 0 #calculo sobre el total de servicios


    total_servicios = 0
    reserva_servicios = ReservaServicio.objects.filter(reserva=reserva)

    # Iterar sobre cada formulario en el formset
    for reserva_servicio in reserva_servicios:
        servicio = reserva_servicio.servicio
        total_servicios += servicio.precio
        

        total_reserva = total_cabania + total_servicios #calculo sobre el total de la reserva
        print(total_servicios)

    context = {
            'reserva': reserva,
            'cabania': cabania,
            'cantidad_dias': cantidad_dias,
            'total_cabania': total_cabania,
            'total_servicios': total_servicios,
            'total_reserva': total_reserva,
            'total_servicios': total_servicios
        }


    return render(request, 'detalle_reserva.html', context)

def detalle_servicio(request, servicio_id):
    servicio = Servicio.objects.get(id=servicio_id)

    context = {
        'servicio': servicio
    } 
    return render(request, 'detalle_servicio.html', context)

#VISTAS ENCARGADO

class lista_encargados(LoginRequiredMixin, ListView):
    login_url = '/login/'
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

class nuevo_encargado(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Encargado
    form_class = formEncargado
    template_name = 'form_encargado.html'
    success_url = reverse_lazy('lista_encargados')

class modif_encargado(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Encargado
    form_class = formEncargado
    template_name = 'form_encargado.html'
    success_url = reverse_lazy('lista_encargados')

class borrar_encargado(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    model = Encargado
    template_name = 'conf_borrar_encargado.html'
    success_url = reverse_lazy('lista_encargados')

#VISTAS DE CABAÑAS

class lista_cabanias(LoginRequiredMixin, ListView):
    login_url = '/login/'
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
    login_url = '/login/'
    model = Cabania
    form_class = formCabania
    template_name = 'form_cabania.html'
    success_url = reverse_lazy('lista_cabanias')

class modif_cabania(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Cabania
    form_class = formCabania
    template_name = 'form_cabania.html'
    success_url = reverse_lazy('lista_cabanias')

class borrar_cabania(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Cabania
    template_name = 'conf_borrar_cabania.html'
    success_url = reverse_lazy('lista_cabanias')
  
#VISTAS DE CLIENTES

class lista_clientes(LoginRequiredMixin, ListView):
    login_url = '/login/'
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
    login_url = '/login/'
    model = Cliente
    form_class = formCliente
    template_name = 'form_cliente.html'
    success_url = reverse_lazy('lista_clientes')

class modif_cliente(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Cliente
    form_class = formCliente
    template_name = 'form_complejo.html'
    success_url = reverse_lazy('lista_clientes')

class borrar_cliente(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Cliente
    template_name = 'conf_borrar_cliente.html'
    success_url = reverse_lazy('lista_clientes')
  
#VISTAS DE COMPLEJO
class lista_complejos(LoginRequiredMixin, ListView):
    login_url = '/login/'
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
    login_url = '/login/'
    model = Complejo
    form_class = formComplejo
    template_name = 'form_complejo.html'
    success_url = reverse_lazy('lista_complejos')

class modif_complejo(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Complejo
    form_class = formComplejo
    template_name = 'form_complejo.html'
    success_url = reverse_lazy('lista_complejos')

class borrar_complejo(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Complejo
    template_name = 'conf_borrar_complejo.html'
    success_url = reverse_lazy('lista_complejos')
    
#VISTAS DE SERVICIOS
class lista_servicios(LoginRequiredMixin, ListView):
    login_url = '/login/'
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
    login_url = '/login/'
    model = Servicio
    form_class = formServicio
    template_name = 'form_servicio.html'
    success_url = reverse_lazy('lista_servicios')

class modif_servicio(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Servicio
    form_class = formServicio
    template_name = 'form_servicio.html'
    success_url = reverse_lazy('lista_servicios')

class borrar_servicio(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Servicio
    template_name = 'conf_borrar_servicio.html'
    success_url = reverse_lazy('lista_servicios')
    
#VISTAS DE RESERVAS
class lista_reservas(LoginRequiredMixin, ListView):
    login_url = '/login/'
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
    
def obtener_id_cliente(apellido_nombre):
    try:
        cliente = Cliente.objects.get(apellido_nombre=apellido_nombre)
        return cliente.id
    except Cliente.DoesNotExist:
        return None
    

class nuevo_reserva(LoginRequiredMixin, CreateView):
    login_url = '/login/'
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

        
    def total_servicios(self):
        total_servicios = 0
        formset = formReserva.ReservaServicioFormset(data=self.request.POST)
        if formset.is_valid():
            for form in formset:
                servicio_id = form.cleaned_data.get('servicio')
                if servicio_id:
                    servicio = Servicio.objects.get(id=servicio_id)
                    total_servicios += servicio.precio
        return total_servicios
    
    def form_valid(self, form):
        cliente_apellido_nombre = form.cleaned_data.get('cliente_apellido_nombre')
        cliente = Cliente.objects.filter(apellido_nombre=cliente_apellido_nombre).first()
    
        if cliente:
            reserva = form.save(commit=False)
            reserva.cliente = cliente
            reserva.save()

            total_servicios = self.total_servicios()

            return super().form_valid(form)
        else:
            form.add_error('cliente_apellido_nombre', 'Cliente no encontrado')
            return self.form_invalid(form)

    def total(self):
        reserva = Reserva.objects.get(pk=id)
        cabania = reserva.cabania.precio
        entrada = reserva.diaEntrada
        salida = reserva.diaSalida

        cantidad_dias = (salida - entrada).days 

        total_cabania = cabania * 2

        total_servicios = 0

        formset = formReserva.ReservaServicioFormset(data=self.request.POST)

                # Iterar sobre cada formulario en el formset
        for servicio_form in formset.forms:
            servicio_id = servicio_form.cleaned_data.get('servicio')
            
            # Verificar si se seleccionó un servicio
            if servicio_id:
                servicio = Servicio.objects.get(id=servicio_id)
                total_servicios += servicio.precio

        context = {
            'reserva': reserva,
            'cabania': cabania,
            'cantidad_dias': cantidad_dias,
            'total_cabania': total_cabania,
            'total_servicios': total_servicios
        }

        return context
        


class modif_reserva(LoginRequiredMixin, UpdateView):
    model = Reserva
    form_class = formReserva
    template_name = 'form_reserva.html'
    success_url = reverse_lazy('lista_reservas')

    def get_initial(self):
        initial = super().get_initial()
        reserva = self.get_object()
        if reserva.cliente:
            initial['cliente_apellido_nombre'] = reserva.cliente.apellido_nombre
        return initial

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

        cliente_apellido_nombre = form.cleaned_data.get('cliente_apellido_nombre')
        cliente = Cliente.objects.filter(apellido_nombre=cliente_apellido_nombre).first()

        if formset.is_valid() and form.is_valid():
            formset.save()

            reserva = form.save(commit=False)
            reserva.cliente = cliente
            reserva.save()
            return super().form_valid(form)
        else:
            form.add_error('cliente_apellido_nombre', 'Cliente no encontrado')
            return self.form_invalid(form)


        
    def total(self):
        reserva = self.object
        cabania = reserva.cabania.precio

        entrada = reserva.diaEntrada #dia entrada
        salida = reserva.diaSalida  #dia salida

        cantidad_dias = (salida - entrada).days #calculo de la diferencia entre dia de entrada y salida

        total_cabania = cabania * cantidad_dias #calculo entre el precio de la cabaña y la cantidad de dias

        total_servicios = 0 #calculo sobre el total de servicios


        total_servicios = 0
        reserva_servicios = ReservaServicio.objects.filter(reserva=reserva)

                # Iterar sobre cada formulario en el formset
        for reserva_servicio in reserva_servicios:
            servicio = reserva_servicio.servicio
            total_servicios += servicio.precio
        

        total_reserva = total_cabania + total_servicios #calculo sobre el total de la reserva
        print(total_servicios)

        total_servicios_reserva = total_servicios * cantidad_dias 

        total_reserva = total_cabania + total_servicios_reserva #calculo sobre el total de la reserva

        context = {
            'reserva': reserva,
            'cabania': cabania,
            'cantidad_dias': cantidad_dias,
            'total_cabania': total_cabania,
            'total_servicios': total_servicios,
            'total_reserva': total_reserva,
            'total_servicios': total_servicios,
            'total_servicios_reserva': total_servicios_reserva
        }

        return context

class borrar_reserva(LoginRequiredMixin, DeleteView):
    model = Reserva
    template_name = 'conf_borrar_reserva.html'
    success_url = reverse_lazy('lista_reservas')


class DetalleReservaServicio(LoginRequiredMixin, ListView):
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


class Hospedaje(View):
    template_name = 'hospedaje.html'

    def get(self, request, *args, **kwargs):
        # Obtén todas las cabañas
        cabañas = Cabania.objects.all()

        # Verifica la disponibilidad de cada cabaña
        disponibilidad_cabañas = []
        today = date.today()
        for cabaña in cabañas:
            # Obtén todas las reservas para la cabaña
            reservas_cabaña = Reserva.objects.filter(cabania=cabaña)

            # Verifica si la cabaña está ocupada en alguna de las reservas existentes
            ocupada = any(
                reserva.diaEntrada <= today <= reserva.diaSalida or
                reserva.diaEntrada <= today <= reserva.diaSalida
                for reserva in reservas_cabaña
            )

            # Obtiene las fechas de ocupación y el cliente asociado a la última reserva
            fechas_ocupacion = [
                {'diaEntrada': reserva.diaEntrada, 'diaSalida': reserva.diaSalida, 'cliente': reserva.cliente}
                for reserva in reservas_cabaña
            ]

            # Calcula las fechas de disponibilidad
            fechas_libres = [fecha['diaSalida'] for fecha in fechas_ocupacion if fecha['diaSalida'] > today]
            if fechas_libres:
                ultima_fecha_salida = min(fechas_libres)
            else:
                ultima_fecha_salida = None

            fechas_proximas = [fecha['diaEntrada'] for fecha in fechas_ocupacion if fecha['diaEntrada'] > today]
            if fechas_proximas:
                ultima_fecha_entrada = min(fechas_proximas)
            else:
                ultima_fecha_entrada = None

            # Agrega la cabaña, su disponibilidad y las fechas de ocupación a la lista
            disponibilidad_cabañas.append({
                'cabaña': cabaña,
                'disponible': not ocupada,
                'fechas_ocupacion': fechas_ocupacion,
                'disponible_desde': ultima_fecha_salida,
                'disponible_hasta': ultima_fecha_entrada
            })

        # Pasa la lista de disponibilidad al contexto del template
        context = {'disponibilidad_cabañas': disponibilidad_cabañas}
        return render(request, self.template_name, context)

'''
from reportlab.pdfbase import pdfmetrics
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from django.shortcuts import get_object_or_404
from reportlab.pdfbase.ttfonts import TTFont

def draw_header(c):
    # Aquí puedes dibujar el contenido del encabezado
    c.setFont("Poppins", 16)
    c.drawString(inch, 10 * inch, "Nombre de tu Empresa")
    # Otros elementos del encabezado...

def factura(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)

    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4, bottomup=0)

    pdfmetrics.registerFont(TTFont('Poppins', 'reservas/static/fonts/Poppins-Regular.ttf'))

    c.setFont("Poppins", 12)
    line_height = 14
    left_margin = inch
    top_margin = inch * 10

    draw_header(c)

    c.drawString(left_margin, top_margin, "Factura")
    top_margin -= line_height * 2

    c.drawString(left_margin, top_margin, f"Cliente: {reserva.cliente}")
    top_margin -= line_height
    c.drawString(left_margin, top_margin, f"Complejo: {reserva.complejo}")
    top_margin -= line_height
    c.drawString(left_margin, top_margin, f"Cabaña: {reserva.cabania}")
    top_margin -= line_height * 2

    c.drawString(left_margin, top_margin, "Detalles:")
    top_margin -= line_height

    cabania = reserva.cabania.precio
    entrada = reserva.diaEntrada
    salida = reserva.diaSalida
    cantidad_dias = (salida - entrada).days
    total_cabania = cabania * cantidad_dias
    total_servicios = 0
    reserva_servicios = ReservaServicio.objects.filter(reserva=reserva)

    # Iterar sobre cada formulario en el formset
    for reserva_servicio in reserva_servicios:
        servicio = reserva_servicio.servicio
        total_servicios += servicio.precio
        

        total_reserva = total_cabania + total_servicios #calculo sobre el total de la reserva

    total_servicios_reserva = total_servicios * cantidad_dias
    total_reserva = total_cabania + total_servicios_reserva
    
    detalles = [
        f"Día de Entrada: {reserva.diaEntrada}",
        f"Día de Salida: {reserva.diaSalida}",
        f"Seña: {reserva.seña}",
        f"total servicios de la reserva: {total_servicios_reserva}",
        f"total servicios por dia: {total_servicios} ",
        f"total reserva: {total_reserva}"
    ]

    for detalle in detalles:
        c.drawString(left_margin, top_margin, detalle)
        top_margin -= line_height

    c.line(left_margin, top_margin, inch + 500, top_margin)
    top_margin -= line_height * 2


    c.drawString(left_margin, top_margin, f"Total: {total_reserva}")

    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename=f'reserva{reserva_id}_factura.pdf')
'''

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from django.shortcuts import get_object_or_404
import io
from django.http import FileResponse

def factura(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)

    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter)

    # Registro de la fuente
    pdfmetrics.registerFont(TTFont('Poppins', 'reservas/static/fonts/Poppins-Regular.ttf'))

    # Configuración de la fuente y márgenes
    c.setFont("Poppins", 12)
    line_height = 14
    left_margin = inch
    top_margin = inch * 10

    # Encabezado
    palabra = "ReserVas"
    mitad1 = palabra[:len(palabra)-3]
    mitad2 = palabra[len(palabra)-3:]

    c.setFillColorRGB(0,0,0)  # Color negro para la primera mitad
    c.drawString(250, 750, mitad1)

    c.setFillColorRGB(147, 128, 255)  # Color azul para la segunda mitad
    c.drawString(283, 750, mitad2)

    # Datos del complejo y cabaña
    c.setFillColorRGB(0, 0, 0)
    complejo_cabania = f"Complejo: {reserva.complejo}   Cabaña: {reserva.cabania}"
    c.drawString(left_margin, 700, complejo_cabania)

    # Detalles de la reserva
    detalles = [
        f"Cliente: {reserva.cliente}",
        f"Día de Entrada: {reserva.diaEntrada}",
        f"Día de Salida: {reserva.diaSalida}",
        f"Seña: {reserva.seña}"
    ]

    # Posición inicial para los detalles de la reserva
    top_margin -= 100

    # Dibujar detalles de la reserva
    for detalle in detalles:
        c.drawString(left_margin, top_margin, detalle)
        top_margin -= line_height

    # Cálculos de precios y total de reserva
    cabania = reserva.cabania.precio
    entrada = reserva.diaEntrada
    salida = reserva.diaSalida
    cantidad_dias = (salida - entrada).days
    total_cabania = cabania * cantidad_dias

    total_servicios = 0
    reserva_servicios = ReservaServicio.objects.filter(reserva=reserva)

    for reserva_servicio in reserva_servicios:
        servicio = reserva_servicio.servicio
        total_servicios += servicio.precio

    total_servicios_reserva = total_servicios * cantidad_dias
    total_reserva = total_cabania + total_servicios_reserva

    # Mostrar totales
    c.drawString(left_margin, top_margin - 30, f"total de los servicios por dia: {total_servicios}")
    c.drawString(left_margin, top_margin - 50, f"Total servicios de la reserva: {total_servicios_reserva}")
    c.drawString(left_margin, top_margin - 70, f"Total reserva: {total_reserva}")

    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename=f'reserva{reserva_id}_factura.pdf')


from django.http import JsonResponse

def search_clients(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        q = request.GET.get('term', '')
        clients = Cliente.objects.filter(apellido_nombre__icontains=q)
        results = [client.apellido_nombre for client in clients]
        return JsonResponse(results, safe=False)



