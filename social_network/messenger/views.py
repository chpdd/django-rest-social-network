from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import mixins

from django.shortcuts import render
from django.db.models import Q

from .models import Chat, GroupChat
from .serializers import ChatSerializer, GroupChatSerializer


class ChatViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Chat.objects.filter(Q(member1=self.request.user.profile) | Q(member2=self.request.user.profile))


class GroupChatViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin, mixins.CreateModelMixin):
    serializer_class = GroupChatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return GroupChat.objects.filter(members=self.request.user.profile)
