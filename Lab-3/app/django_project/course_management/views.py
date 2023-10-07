from django.shortcuts import render, redirect
from .models import Asignatura, Alumno
from .forms import AsignaturaForm, AlumnoForm
from django.shortcuts import render, get_object_or_404, redirect

def lista_asignaturas(request):
    asignaturas = Asignatura.objects.all()
    return render(request, 'lista_asignaturas.html', {'asignaturas': asignaturas})

def eliminar_alumno(request, asignatura_id, alumno_id):
    asignatura = get_object_or_404(Asignatura, pk=asignatura_id)
    alumno = get_object_or_404(Alumno, pk=alumno_id)

    if request.method == 'POST':
        # Elimina al alumno de la asignatura
        asignatura.alumno_set.remove(alumno)
        return redirect('detalle_asignatura', asignatura_id=asignatura.id)

    return render(request, 'eliminar_alumno.html', {'asignatura': asignatura, 'alumno': alumno})


def crear_asignatura(request):
    if request.method == 'POST':
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_asignaturas')
    else:
        form = AsignaturaForm()
    return render(request, 'crear_asignatura.html', {'form': form})

def editar_asignatura(request, asignatura_id):
    asignatura = Asignatura.objects.get(id=asignatura_id)
    if request.method == 'POST':
        form = AsignaturaForm(request.POST, instance=asignatura)
        if form.is_valid():
            form.save()
            return redirect('lista_asignaturas')
    else:
        form = AsignaturaForm(instance=asignatura)
    return render(request, 'editar_asignatura.html', {'form': form, 'asignatura': asignatura})

def eliminar_asignatura(request, asignatura_id):
    asignatura = Asignatura.objects.get(id=asignatura_id)
    if request.method == 'POST':
        asignatura.delete()
        return redirect('lista_asignaturas')
    return render(request, 'eliminar_asignatura.html', {'asignatura': asignatura})

def detalle_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, pk=asignatura_id)
    # Lógica adicional si es necesario
    return render(request, 'detalle_asignatura.html', {'asignatura': asignatura})

def agregar_alumnos(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, pk=asignatura_id)

    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.save()  # Guarda el alumno primero
            asignatura.alumno_set.add(alumno)  # Agrega el alumno a la asignatura
            return redirect('detalle_asignatura', asignatura_id=asignatura.id)
    else:
        form = AlumnoForm()

    return render(request, 'agregar_alumno.html', {'form': form, 'asignatura': asignatura})