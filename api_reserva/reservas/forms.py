from django import forms
from .models import Cabania

class formCabania(forms.ModelForm):
    class Meta:
        model = Cabania
        fields = ('nombre', 'tipo', 'capacidad', 'precio', 'complejo')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.NumberInput(attrs={'class': 'form-control'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'from-control'}),
            'complejo': forms.TextInput(attrs={'class': 'form-control'}),
        }
