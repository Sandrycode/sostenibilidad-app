from django.urls import path
from . import views



urlpatterns = [
    path('', views.lista_tareas, name='agenda_home'),
    path('tareas/', views.lista_tareas, name='lista_tareas'),
    path('agregar/', views.agregar_tarea, name='agregar_tarea'),
    path('editar/<int:tarea_id>/', views.editar_tarea, name='editar_tarea'),
    path('eliminar/<int:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea'),
]

