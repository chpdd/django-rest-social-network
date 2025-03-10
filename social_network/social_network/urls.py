from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from accounts.views import ProfileViewSet
from publications.views import PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r"profile", ProfileViewSet, basename="profile")
router.register(r"post", PostViewSet, basename="post")
router.register(r"comment", CommentViewSet, basename="comment")

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'', include(router.urls)),
]
