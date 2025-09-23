# Create your models here.

from django.db import models

class Diagnostico(models.Model):
    nombre_empresa = models.CharField("Nombre de la empresa", max_length=100, blank=False)
    sector = models.CharField("Sector de actividad", max_length=100, blank=False)
    fecha = models.DateTimeField(auto_now_add=True)

    # ISO 14001 - Gestión ambiental
    tiene_politica_ambiental = models.BooleanField("¿La empresa tiene una política ambiental?", blank=False)
    cumple_normativa_local = models.BooleanField("¿Cumple con la normativa ambiental local?", blank=False)
    realiza_auditorias = models.BooleanField("¿Realiza auditorías ambientales periódicas?", blank=False)
    gestiona_residuos = models.BooleanField("¿Gestiona adecuadamente sus residuos?", blank=False)
    usa_energia_renovable = models.BooleanField("¿Utiliza fuentes de energía renovable?", blank=False)
    mide_consumo_agua = models.BooleanField("¿Mide y controla el consumo de agua?", blank=False)
    tiene_plan_emergencia = models.BooleanField("¿Tiene plan de emergencia ambiental?", blank=False)

    # ISO 26000 - Responsabilidad social
    involucra_empleados = models.BooleanField("¿Involucra a los empleados en prácticas sostenibles?", blank=False)
    comunica_transparente = models.BooleanField("¿Comunica de forma transparente sus acciones?", blank=False)
    colabora_comunidad = models.BooleanField("¿Colabora con la comunidad local?", blank=False)
    promueve_igualdad = models.BooleanField("¿Promueve la igualdad y diversidad?", blank=False)
    evalua_proveedores = models.BooleanField("¿Evalúa la sostenibilidad de sus proveedores?", blank=False)

    # Campo opcional
    observaciones = models.TextField("Observaciones adicionales", blank=True, null=True)



    def puntaje_total(self):
        respuestas = [
            self.tiene_politica_ambiental,
            self.cumple_normativa_local,
            self.realiza_auditorias,
            self.gestiona_residuos,
            self.usa_energia_renovable,
            self.mide_consumo_agua,
            self.tiene_plan_emergencia,
            self.involucra_empleados,
            self.comunica_transparente,
            self.colabora_comunidad,
            self.promueve_igualdad,
            self.evalua_proveedores
        ]
        return sum(respuestas)

    def nivel_sostenibilidad(self):
        puntaje = self.puntaje_total()
        if puntaje >= 10:
            return "Alto"
        elif puntaje >= 6:
            return "Medio"
        else:
            return "Bajo"

    def __str__(self):
        return f"{self.nombre_empresa} ({self.fecha.date()})"
    
    def puntaje_iso_14001(self):
        criterios = [
        self.tiene_politica_ambiental,
        self.cumple_normativa_local,
        self.realiza_auditorias,
        self.gestiona_residuos,
        self.usa_energia_renovable,
        self.mide_consumo_agua,
        self.tiene_plan_emergencia,
    ]
        return int(sum(criterios))

    def puntaje_iso_26000(self):
        criterios = [
            self.involucra_empleados,
            self.comunica_transparente,
            self.colabora_comunidad,
            self.promueve_igualdad,
            self.evalua_proveedores,
        ]
        return int(sum(criterios))

    def dictamen_tecnico(self):
        ambiental = self.puntaje_iso_14001()
        social = self.puntaje_iso_26000()

    # Evaluación ambiental
        if ambiental >= 6:
            iso_14001 = "Cumplimiento Alto"
            recomendacion_ambiental = (
                "La empresa demuestra un sólido compromiso ambiental. "
                "Se recomienda mantener las prácticas actuales y explorar certificaciones adicionales como ISO 50001 (gestión energética)."
            )
        elif ambiental >= 4:
            iso_14001 = "Cumplimiento Medio"
            recomendacion_ambiental = (
                "La empresa cumple con varios criterios ambientales, pero aún hay margen de mejora. "
                "Se sugiere implementar auditorías internas y reforzar la gestión de residuos."
            )
        else:
            iso_14001 = "Cumplimiento Bajo"
            recomendacion_ambiental = (
                "La empresa presenta debilidades en su gestión ambiental. "
                "Se recomienda desarrollar una política ambiental formal y establecer indicadores de seguimiento."
            )

    # Evaluación social
        if social >= 4:
            iso_26000 = "Cumplimiento Alto"
            recomendacion_social = (
                "La empresa tiene una cultura organizacional responsable. "
                "Se recomienda compartir buenas prácticas con proveedores y fortalecer la comunicación externa."
            )
        elif social >= 3:
            iso_26000 = "Cumplimiento Medio"
            recomendacion_social = (
                "La empresa muestra avances en responsabilidad social, pero puede mejorar. "
                "Se sugiere involucrar más activamente a los empleados y evaluar el impacto comunitario."
            )
        else:
            iso_26000 = "Cumplimiento Bajo"
            recomendacion_social = (
                "La empresa necesita fortalecer su enfoque social. "
                "Se recomienda establecer políticas de igualdad, diversidad y colaboración comunitaria."
            )

        return {
            "ISO_14001": {
                "puntaje": ambiental,
                "nivel": iso_14001,
                "recomendacion": recomendacion_ambiental
            },
            "ISO_26000": {
                "puntaje": social,
                "nivel": iso_26000,
                "recomendacion": recomendacion_social
            }
        }
