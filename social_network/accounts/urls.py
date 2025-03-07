from django.urls import path, include
from rest_framework import routers

from .views import ProfileViewSet

app_name = "accounts"

router = routers.SimpleRouter()
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path("", include(router.urls))
]