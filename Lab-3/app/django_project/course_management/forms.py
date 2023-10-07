from django import forms
from .models import Asignatura, Alumno

class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ['nombre', 'codigo']

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento']