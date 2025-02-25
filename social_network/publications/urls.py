from django.urls import path, include
from rest_framework import routers

from .views import PostViewSet, CommentViewSet

app_name = 'publications'

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]