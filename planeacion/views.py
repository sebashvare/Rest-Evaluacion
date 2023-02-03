from django.urls import reverse
from rest_framework.decorators import api_view
from .serializer import HacerSerializer, PlaneacionSerializer
from rest_framework import viewsets
from .models import Hacer, Planeacion, Backlog
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers


class getPlaneacion(viewsets.ModelViewSet):
    queryset = Planeacion.objects.all()
    serializer_class = PlaneacionSerializer


class getHacer(viewsets.ModelViewSet):
    queryset = Hacer.objects.all()
    serializer_class = HacerSerializer


def listPlaneacion(request):
    listado_planeacion = Planeacion.objects.all()
    return render(request, "planeacion/formulario_planeacion.html", {"data": listado_planeacion})


def list_backlog(request):
    data = Backlog.objects.all()
    return render(request, "eventos/listar_eventos.html", {"data": data})


def list_backlog_json(request):
    data = Backlog.objects.all()
    json = serializers.serialize('json', data)
    return HttpResponse(json, content_type='application/json')


def registrar_eventos(request):
    return render(request, "eventos/registrar_eventos.html", {})


def save_eventos(request):
    
    if request.method == "POST":
        
        
        quienReporta = request.POST.get("quienReporta")
        print(quienReporta)
        idPuntoServicio = request.POST.get("idPuntoServicio")
        actividadEjecutar = request.POST.get("actividadEjecutar")
        fuente = request.POST.get("fuente")
        contrata = request.POST.get("contrata")
        quienResuelve = request.POST.get("quienResuelve")

        data = Backlog(
            fuente=quienReporta,
            reporte = actividadEjecutar,         
            id_punto_servicio = idPuntoServicio,
            ejecucion = fuente,
            responsable = quienResuelve,
            contrata = contrata
        )
        data.save()
        data = Backlog.objects.all()
        agregado = True
    return render(request, "eventos/listar_eventos.html", {"data": data, "info":agregado})
