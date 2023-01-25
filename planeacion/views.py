from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import HacerSerializer, PlaneacionSerializer
from rest_framework import viewsets
from .models import Hacer, Planeacion


class getPlaneacion(viewsets.ModelViewSet):
    queryset = Planeacion.objects.all()
    serializer_class = PlaneacionSerializer

class getHacer(viewsets.ModelViewSet):
    queryset = Hacer.objects.all()
    serializer_class = HacerSerializer
