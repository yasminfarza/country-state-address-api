from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register('countries', views.CountryViewSet)
router.register('states/(?P<country>[^/.]+)', views.StateViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls))
]
