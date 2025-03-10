from django.urls import path, include
from rest_framework import routers

from .views import ProfileViewSet

app_name = "accounts"

router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet)

urlpatterns = [
    path("", include(router.urls))
]