from django.contrib import admin
from .models import Hacer,Planeacion, Evaluacion, Backlog, Confiabilidad


admin.site.register(Hacer)
admin.site.register(Planeacion)
admin.site.register(Evaluacion)
admin.site.register(Backlog)
admin.site.register(Confiabilidad)
