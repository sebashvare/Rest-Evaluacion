from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = "planeacion"

router = DefaultRouter()
router.register("api/planeacion", views.getPlaneacion)
router.register("api/hacer", views.getHacer)

urlpatterns = [
    path("eventos", views.list_backlog, name="list_backlog"),
    path("regevento", views.registrar_eventos, name="registrar_eventos"),
    path("saveEvento", views.save_eventos, name="save_event"),
    path("planeacion", views.save_planeacion, name="save_planeacion"),
    path("regeplaneacion", views.registrar_planeacion, name="reg_planeacion"),
    path("listPlaneacion", views.listPlaneacion, name="listPlaneacion"),
]


urlpatterns += router.urls