from django.contrib import admin
from .models import Hacer, Planeacion, Evaluacion, Backlog, Confiabilidad


@admin.register(Hacer)
class HacerAdmin(admin.ModelAdmin):
    list_display = ("orden_trabajo", "actividad_ejecutada", "numero_formato",
                    "multiplo", "telemedida", "actualizac0ion_sistema", "pagar")
    list_display_links = ("orden_trabajo", "numero_formato")
    list_filter = ("orden_trabajo", "pagar")
    search_fields = ("actividad_ejecutada", "pagar",
                     "orden_trabajo__orden_trabajo")


@admin.register(Planeacion)
class PlaneacionAdmin(admin.ModelAdmin):
    list_display = ("orden_trabajo", "fuente", "contrata",
                    "fecha_programacion", "estado")
    list_display_links = ("orden_trabajo", "estado")
    list_filter = ("contrata", "estado")
    search_fields = ("orden_trabajo", "fuente", "contrata")


@admin.register(Evaluacion)
class EvaluacionAdmin(admin.ModelAdmin):
    list_display = ("orden_trabajo", "primera_factura",
                    "ultima_telemedida", "conforme")
    list_display_links = ("orden_trabajo", "conforme")


@admin.register(Backlog)
class BacklogAdmin(admin.ModelAdmin):
    list_display = ("id", "fecha", "fuente", "reporte", "id_punto_servicio",
                    "ejecucion", "estado", "responsable", "contrata")
    list_filter = ("fecha", "fuente", "reporte", "id_punto_servicio",
                   "ejecucion", "estado", "responsable", "contrata")
    list_display_links = ("id_punto_servicio", "estado")


@admin.register(Confiabilidad)
class ConfiabilidadAdmin(admin.ModelAdmin):
    list_display = (
        "orden_trabajo",
        "valor_tensiones",
        "valor_corrientes",
        "sincro_fecha",
        "validacion_canales",
        "cargue_fasorial",
    )
    list_filter = (
        "orden_trabajo",
        "valor_tensiones",
        "valor_corrientes",
        "sincro_fecha",
        "validacion_canales",
        "cargue_fasorial",
    )

    search_fields = (
        "orden_trabajo__orden_trabajo",
        "validacion_canales",
    )
