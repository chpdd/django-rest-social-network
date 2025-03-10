from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import mixins
from rest_framework import permissions

from .models import Profile
from .serializers import ProfileSerializer
from .permissions import IsOwnerOrReadOnly


class ProfileViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin,
                     mixins.UpdateModelMixin):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    # def get_queryset(self):
    #     return Profile.objects.filter(user=self.request.user)
