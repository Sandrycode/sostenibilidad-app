from django.db import models
from django.contrib.auth.models import User  # ← importa el modelo de usuario

class Tarea(models.Model):
    descripcion = models.CharField(max_length=255)
    fecha = models.DateTimeField(null=True, blank=True)
    prioridad = models.CharField(
        max_length=10,
        choices=[("baja", "Baja"), ("media", "Media"), ("urgente", "Urgente")],
        default="media"
    )
    completada = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # ← este es el nuevo campo

    def __str__(self):
        return self.descripcion

    def hora(self):
        return self.fecha.strftime('%H:%M') if self.fecha else ''



