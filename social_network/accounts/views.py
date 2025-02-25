from rest_framework import viewsets, mixins, permissions, generics
from django.contrib.auth import get_user_model

from .serializers import ProfileSerializer, UserSerializer
from .models import Profile
from .permissions import IsNotAuthenticated, IsUserOrClose, IsUserOrReadOnly


# class ProfileViewSet(viewsets.GenericViewSet,
#                     mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsUserOrReadOnly & permissions.IsAuthenticated]

class UserViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUserOrReadOnly & permissions.IsAuthenticated]
