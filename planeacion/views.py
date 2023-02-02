from rest_framework.response import Response
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
