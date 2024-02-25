from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


# Create a router and register the viewsets
router = DefaultRouter()

router.register(r'auth?', AuthViewSet, basename='auth')

urlpatterns = [
    path('', include(router.urls)),
]
