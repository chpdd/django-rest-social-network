from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'accounts'

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
