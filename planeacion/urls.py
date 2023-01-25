from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("api/planeacion", views.getPlaneacion)
router.register("api/hacer", views.getHacer)

urlpatterns = router.urls