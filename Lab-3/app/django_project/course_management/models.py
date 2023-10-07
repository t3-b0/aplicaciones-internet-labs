from django.db import models
from django.utils.text import slugify

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'course_management'  # Nombre de la aplicación
    def __str__(self):
        return self.nombre
    def save(self, *args, **kwargs):
        # Generar un código único basado en el nombre de la asignatura
        if not self.codigo:
            self.codigo = slugify(self.nombre)
        super(Asignatura, self).save(*args, **kwargs)

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    asignaturas = models.ManyToManyField(Asignatura, blank=True)
    class Meta:
        app_label = 'course_management'  # Nombre de la aplicación
    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"