# Create your views here.
from django.shortcuts import render, redirect

from django.shortcuts import render
from .models import Tarea
from .forms import TareaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def lista_tareas(request):
    estado = request.GET.get('estado')
    if estado == 'pendientes':
        tareas = Tarea.objects.filter(usuario=request.user, completada=False).order_by('fecha')
    elif estado == 'completadas':
        tareas = Tarea.objects.filter(usuario=request.user, completada=True).order_by('fecha')
    else:
        tareas = Tarea.objects.filter(usuario=request.user).order_by('fecha')
    return render(request, 'agenda/lista_tareas.html', {
        'tareas': tareas,
        'messages': messages.get_messages(request)
    })




@login_required(login_url='login')
def agregar_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.usuario = request.user  # ← asigna el usuario actual
            tarea.save()
            messages.success(request, 'Tarea agregada correctamente.')
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    return render(request, 'agenda/agregar_tarea.html', {'form': form})




@login_required(login_url='login')
def editar_tarea(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    if tarea.usuario != request.user:
        messages.error(request, 'No tienes permiso para editar esta tarea.')
        return redirect('lista_tareas')

    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarea actualizada correctamente.')
            return redirect('lista_tareas')
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'agenda/editar_tarea.html', {'form': form})




@login_required(login_url='login')
def eliminar_tarea(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    if tarea.usuario != request.user:
        messages.error(request, 'No tienes permiso para eliminar esta tarea.')
        return redirect('lista_tareas')

    if request.method == 'POST':
        tarea.delete()
        messages.success(request, 'Tarea eliminada correctamente.')
        return redirect('lista_tareas')
    return render(request, 'agenda/eliminar_tarea.html', {'tarea': tarea})



def inicio(request):
    return render(request, 'agenda/inicio.html', {'mostrar_menu': False})





