from django.contrib import admin
from django.urls import path, re_path, include

from rest_framework import routers, permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from accounts.views import ProfileViewSet
from publications.views import PostViewSet, CommentViewSet

schema_view = get_schema_view(info=openapi.Info(title="API Documentations", default_version="v1", description="Документация для API"), public=True, permission_classes=[permissions.AllowAny])

router = routers.DefaultRouter()
router.register(r"profile", ProfileViewSet, basename="profile")
router.register(r"post", PostViewSet, basename="post")
router.register(r"comment", CommentViewSet, basename="comment")

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'', include(router.urls)),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
