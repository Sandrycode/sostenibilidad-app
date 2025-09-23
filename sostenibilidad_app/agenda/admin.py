# Register your models here.

from django.contrib import admin
from .models import Tarea

class TareaAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'fecha', 'hora', 'prioridad', 'completada')
    list_filter = ('completada', 'prioridad')
    search_fields = ('descripcion',)

admin.site.register(Tarea, TareaAdmin)



