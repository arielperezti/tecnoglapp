from django.db import models

# Create your models here.
# (Nombre, Cédula, Fecha de Nacimiento, Email, Número de teléfono)

class Empleado(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    cedula = models.IntegerField()
    fechaNac = models.DateField()
    email = models.EmailField(max_length=45)
    telefono = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre + " " + self.apellido
    

