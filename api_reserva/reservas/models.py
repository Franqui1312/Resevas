from django.db import models

# Create your models here.

class Cliente(models.Model):
    apellido_nombre = models.CharField(max_length=100)
    dni = models.IntegerField(default=0)
    telefono = models.CharField(max_length=30)
    email = models.CharField(max_length=50, default="user@gmail.com")
    pais = models.CharField(max_length=30, default="Argentina")
    provincia = models.CharField(max_length=30, default="Cordoba")
    localidad = models.CharField(max_length=30, default="Cordoba")

    def __str__(self):
        return self.apellido_nombre

class Encargado(models.Model):
    apellido_nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=30)
    email = models.CharField(max_length=50, default="user@gmail.com")

    def __str__(self):
        return self.apellido_nombre

class Servicio(models.Model):
    codigo = models.CharField(default="nada", max_length=20)
    descripcion = models.CharField(default="nada", max_length=150)
    precio = models.FloatField(default=0, max_length=20)
    #incluido = models.CharField(default="no",max_length=20, choices=[('si','si'),('no','no')])

    def __str__(self):
        return self.codigo

class Complejo(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    encargado = models.ForeignKey(Encargado, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre


class Cabania(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=15, choices=[('Apart','Apart'), ('Cabaña', 'Cabaña'), ('Departamento','Departamento'), ('Habitacion','Habitacion')])
    capacidad = models.CharField(max_length=2)
    precio = models.FloatField(max_length=10)
    complejo = models.ForeignKey(Complejo, on_delete=models.CASCADE, default="none")

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    complejo = models.ForeignKey(Complejo, on_delete=models.CASCADE)
    cabania = models.ForeignKey(Cabania, on_delete=models.CASCADE, default=None)
    diaEntrada = models.DateField()
    diaSalida = models.DateField()
    servicios = models.ForeignKey(Servicio, on_delete=models.CASCADE, default=None)
    seña = models.FloatField(default=0, max_length=12)
    precio = models.FloatField(default=0,max_length=12)

    def __str__(self):
        return self.cliente.apellido_nombre
    
