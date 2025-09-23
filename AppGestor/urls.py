from django.urls import path
from AppGestor import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('alumnoFormulario/', views.alumnoFormulario, name="alumnoFormulario"),
    path('asistenciaFormulario/', views.asistenciaFormulario, name="asistenciaFormulario"),
    path('trabajoFormulario/', views.trabajoFormulario, name="trabajoFormulario"),
    path('buscarAlumno/', views.buscarAlumno, name="buscarAlumno"),
]
