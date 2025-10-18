from django.urls import path
from AppGestor import views

from .views import (
    AlumnoListView, AlumnoDetailView,
    AlumnoCreateView, AlumnoUpdateView, AlumnoDeleteView
)

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('alumnoFormulario/', views.alumnoFormulario, name="alumnoFormulario"),
    path('asistenciaFormulario/', views.asistenciaFormulario, name="asistenciaFormulario"),
    path('trabajoFormulario/', views.trabajoFormulario, name="trabajoFormulario"),
    path('buscarAlumno/', views.buscarAlumno, name="buscarAlumno"),
    #Crud Alumno
    path('alumnos/', AlumnoListView.as_view(), name='alumno_list'),
    path('alumnos/<int:pk>/', AlumnoDetailView.as_view(), name='alumno_detail'),
    path('alumnos/crear/', AlumnoCreateView.as_view(), name='alumno_create'),
    path('alumnos/<int:pk>/editar/', AlumnoUpdateView.as_view(), name='alumno_update'),
    path('alumnos/<int:pk>/borrar/', AlumnoDeleteView.as_view(), name='alumno_delete'),
    #Vista asistencias
    path('asistencias/', views.listado_asistencias, name='listado_asistencias'),

]
