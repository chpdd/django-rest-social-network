from django.urls import path, include
from rest_framework import routers

from .views import PublicationViewSet, CommentViewSet

app_name = "publications"

router = routers.SimpleRouter()
router.register(r'publications', PublicationViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path("", include(router.urls))
]