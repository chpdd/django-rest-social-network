from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.viewsets import mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from publications.models import Post
from publications.serializers import PostSerializer
from .models import Profile, Subscription
from .serializers import ProfileSerializer
from .permissions import ActualUserOrReadOnly, NotActualUser


class ProfileViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin,
                     mixins.UpdateModelMixin):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [ActualUserOrReadOnly]

    @action(["post"], detail=True, permission_classes=[NotActualUser])
    def subscribe(self, request, pk=None):
        subscriber = request.user.profile
        subscribed_to = self.get_object()

        _, created = Subscription.objects.get_or_create(subscriber=subscriber, subscribed_to=subscribed_to)

        if created:

            return Response(data={"detail": "You have successfully subscribed"}, status=status.HTTP_201_CREATED)
        return Response(data={"detail": "You've already been subscribed"}, status=status.HTTP_200_OK)

    @action(["delete"], detail=True, permission_classes=[NotActualUser])
    def unsubscribe(self, request, pk=None):
        subscriber = request.user.profile
        subscribed_to = self.get_object()

        subscription = Subscription.objects.filter(subscriber=subscriber, subscribed_to=subscribed_to)

        if subscription.exists():
            subscription.delete()
            return Response(data={"detail": "You have successfully unsubscribe"}, status=status.HTTP_204_NO_CONTENT)
        return Response(data={"detail": "You weren't subscribed"}, status=status.HTTP_200_OK)

    @action(methods=["get"], detail=True)
    def posts(self, request, pk):
        owner = self.get_object()
        posts = Post.objects.filter(owner=owner)
        serializer = PostSerializer(posts, many=True, context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

