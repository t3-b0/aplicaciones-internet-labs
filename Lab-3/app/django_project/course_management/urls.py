from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_asignaturas, name='lista_asignaturas_root'),
    path('asignaturas/', views.lista_asignaturas, name='lista_asignaturas'),
    path('asignaturas/crear/', views.crear_asignatura, name='crear_asignatura'),
    path('asignaturas/editar/<int:asignatura_id>/', views.editar_asignatura, name='editar_asignatura'),
    path('asignaturas/eliminar/<int:asignatura_id>/', views.eliminar_asignatura, name='eliminar_asignatura'),
    path('asignaturas/<int:asignatura_id>/agregar_alumnos/', views.agregar_alumnos, name='agregar_alumnos'),
    path('asignaturas/<int:asignatura_id>/', views.detalle_asignatura, name='detalle_asignatura'),
    path('asignaturas/<int:asignatura_id>/eliminar_alumno/<int:alumno_id>/', views.eliminar_alumno, name='eliminar_alumno'),
    # Define las URL para las operaciones con alumnos (crear, editar, eliminar)
]