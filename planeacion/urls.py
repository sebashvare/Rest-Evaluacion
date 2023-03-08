from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.views.static import serve

from . import views

app_name = "planeacion"

router = DefaultRouter()
router.register("api/planeacion", views.getPlaneacion)
router.register("api/hacer", views.getHacer)

urlpatterns = [
    path("eventos/", views.list_backlog, name="list_backlog"),
    path("regevento/", views.registrar_eventos, name="registrar_eventos"),
    path("saveEvento/", views.save_eventos, name="save_event"),
    path("planeacion/", views.save_planeacion, name="save_planeacion"),
    path("regeplaneacion/", views.registrar_planeacion, name="reg_planeacion"),
    path("listPlaneacion/", views.listPlaneacion, name="listPlaneacion"),
    path("listhacer/", views.list_hacer, name="listhacer"),
    path("regehacer/", views.registrar_hacer, name="regehacer"),
    path("hacer/", views.save_hacer, name="save_hacer"),
    path("evaluacion/", views.list_evaluacion, name="evaluacion"),
    path("regevaluacion/", views.registrar_evaluacion, name="rege_evaluacion"),
    path("saveevaluacion/", views.save_evaluacion, name="save_evaluacion"),
    path("listconfiabilidad/", views.list_confiabilidad, name="listconfiabilidad"),
    path("regconfiabilidad/", views.registrar_confiabilidad, name="regconfiabilidad"),
    path("user/login/", views.formulario_login, name="login"),
    path("loginapp", views.login_app, name="login_app"),
]


urlpatterns += router.urls
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve,{
        'document_root': settings.MEDIA_ROOT,
    })
]
