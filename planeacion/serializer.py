from rest_framework import serializers
from .models import Hacer, Planeacion


class PlaneacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planeacion
        fields = ("__all__")


class HacerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hacer
        fields = ("__all__")
