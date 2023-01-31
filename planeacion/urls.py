from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = "planeacion"

router = DefaultRouter()
router.register("api/planeacion", views.getPlaneacion)
router.register("api/hacer", views.getHacer)

urlpatterns = [
    path("planeacion", views.listPlaneacion, name="list_planeacion"),
    path("eventos", views.list_backlog, name="list_backlog"),
]


urlpatterns += router.urls