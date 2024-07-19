from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BuildingViewSet, SolarDataViewSet

router = DefaultRouter()
router.register(r'buildings', BuildingViewSet)
router.register(r'solardata', SolarDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
