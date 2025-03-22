from rest_framework.decorators import action
from django.shortcuts import render
from rest_framework import viewsets, permissions, mixins, status
from rest_framework.views import Response

from accounts.models import Subscription
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly, NoListIsOwnerOrReadOnly


class PostViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                  mixins.CreateModelMixin, mixins.DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.profile)

    @action(detail=False, methods=["get"])
    def subscriptions_posts(self, request):
        # simple
        # sub_objs = Subscription.objects.filter(subscriber=request.user.profile)
        # sub_profiles = [sub_obj.subscribed_to for sub_obj in sub_objs]
        # or faster
        # sub_profiles = Subscription.objects.filter(subscriber=request.user.profile).values_list("subscribed_to", flat=True)
        subscribed_to = request.user.profile.subscribed_to.all()
        posts = Post.objects.filter(owner__in=subscribed_to).order_by("-pub_date_time")
        serializer = PostSerializer(posts, many=True, context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def like_switch(self, request, pk):
        post = self.get_object()
        profile = request.user.profile
        response = Response(status=status.HTTP_200_OK)
        if profile in post.likers.all():
            post.likers.remove(profile)
            response.data = {"detail": "Like is removed"}
        else:
            post.likers.add(profile)
            response.data = {"detail": "Like it"}
        post.save()
        return response

    @action(detail=True, methods=["get"])
    def comments(self, request, pk):
        post = self.get_object()
        comments = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comments, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def add_comment(self, request, pk):
        post = self.get_object()
        serializer = CommentSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save(owner=request.user.profile, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def like_switch(self, request, pk):
        comment = self.get_object()
        profile = request.user.profile
        response = Response(status=status.HTTP_200_OK)
        if profile in comment.likers.all():
            comment.likers.remove(profile)
            response.data = {"detail": "Like is removed"}
        else:
            comment.likers.add(profile)
            response.data = {"detail": "Like it"}
        comment.save()
        return response

    @action(detail=False, methods=["get"], permission_classes=[permissions.IsAuthenticated])
    def my_comments(self, request):
        comments = request.user.profile.comments.all()
        serializer = CommentSerializer(comments, many=True, context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        post_id = self.request.data.get("post")
        post = Post.objects.get_object_or_404(id=post_id)
        serializer.save(owner=self.request.user.profile, post=post)
