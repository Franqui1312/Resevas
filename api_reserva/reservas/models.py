from django.db import models

# Create your models here.

class Cliente(models.Model):
    dni = models.IntegerField(default=0)
    apellido_nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=30)
    email = models.CharField(max_length=50, default="user@gmail.com")
    pais = models.CharField(max_length=30, default="Argentina")
    provincia = models.CharField(max_length=30, default="Cordoba")
    localidad = models.CharField(max_length=30, default="Cordoba")

    def __str__(self):
        return self.apellido_nombre

class Encargado(models.Model):
    dni = models.IntegerField(default=0)
    apellido_nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=30)
    email = models.CharField(max_length=50, default="user@gmail.com")

    def __str__(self):
        return self.apellido_nombre

class Complejo(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    encargado = models.ForeignKey(Encargado, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre


class Cabania(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=15, choices=[('Apart','Apart'), ('Cabaña', 'Cabaña'), ('Departamento','Departamento'), ('Habitacion','Habitacion')])
    capacidad = models.IntegerField(default=0)
    precio_pers= models.FloatField(default=0)
    precio = models.FloatField(default=0)
    servicio_incluido= models.CharField(default="ninguno",max_length=100)
    complejo = models.ForeignKey(Complejo, on_delete=models.CASCADE, default="none")

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(default="ninguna", max_length=150)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre
class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    complejo = models.ForeignKey(Complejo, on_delete=models.CASCADE)
    cabania = models.ForeignKey(Cabania, on_delete=models.CASCADE, default=None)
    cant_personas = models.IntegerField(default=0)
    servicio= models.ForeignKey(Servicio, on_delete=models.CASCADE, default=None)
    diaEntrada = models.DateField()
    diaSalida = models.DateField()
    seña = models.FloatField(default=0)

    def __str__(self):
        return self.cliente.apellido_nombre
    

class ReservaServicio(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    def __str__(self):
        return f"ReservaServicio {self.id}"
