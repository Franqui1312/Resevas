from django import forms
from django.forms import inlineformset_factory
from .models import Cabania, Encargado, Cliente, Complejo, Reserva, Servicio, ReservaServicio

class formCabania(forms.ModelForm):
    class Meta:
        model = Cabania
        fields = ('nombre', 'tipo', 'capacidad', 'servicio_incluido', 'precio', 'precio_pers', 'complejo')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Nombre de la Cabaña'}),
            'tipo': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Ingrese el tipo de Cabaña'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la capacidad de personas'}),
            'servicio_incluido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese los servicios ya incluidos en la cabaña'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el precio base'}),
            'precio_pers': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el precio por persona'}),
            'complejo': forms.Select(attrs={'class': 'form-select'}),
        }


class formEncargado(forms.ModelForm):
    class Meta:
        model = Encargado
        fields = ('apellido_nombre','dni', 'telefono', 'email')
        widgets = {
            'apellido_nombre': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Ingrese su Nombre y Apellido'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control' , 'placeholder': 'ingrese su DNI'} ),
            'telefono': forms.NumberInput(attrs={'class': 'form-control' , 'placeholder': 'Ingrese su Número Telefónico'}),
            'email': forms.EmailInput(attrs={'class': 'form-control' , 'placeholder': 'Ingrese su Correo Electrónico'}),
        }

class formCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('apellido_nombre', 'dni', 'telefono', 'email', 'pais', 'provincia', 'localidad')
        widgets = {
            'apellido_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Nombre y Apellido'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Número de Documento'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Teléfono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control' , 'placeholder': 'Ingrese su Correo Electrónico'}),
            'pais': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Pais de Origen'}),
            'provincia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Provincia de Origen'}),
            'localidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Localidad de Origen'}),
        }

class formComplejo(forms.ModelForm):
    class Meta:
        model = Complejo
        fields = ('nombre', 'direccion', 'encargado')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Nombre'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la Dirección'}),
            'encargado': forms.Select(attrs={'class': 'form-select'}),
        }
    
class formServicio(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ('nombre', 'descripcion', 'precio')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Nombre'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la Descripción'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Precio'}),
        }

class formReservaServicio(forms.ModelForm):
    
    class Meta:
        model = ReservaServicio
        fields = ('reserva','servicio')
        widgets = {
            'reserva': forms.Select(attrs={'class': 'form-select'}),
            'servicio': forms.Select(attrs={'class': 'form-select'}),
        }

class formReserva(forms.ModelForm):
    
    class Meta:
        model = Reserva
        fields = ('cliente','complejo', 'cabania', 'cant_personas', 'diaEntrada', 'diaSalida','seña', 'servicio')
        widgets = {
            
            'complejo': forms.Select(attrs={'class': 'form-select', 'id': 'complejo-select'}),
            'cabania': forms.Select(attrs={'class': 'form-select', 'id': 'cabania-select'}),
            'cliente':forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione el cliente'}),
            'cant_personas': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la cantidad de personas'}),
            'diaEntrada': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'diaSalida': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'seña': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la Seña'}),
            'servicio': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Seleccione tipo de servicio'}),}
