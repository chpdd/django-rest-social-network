from rest_framework.decorators import action
from django.shortcuts import render
from rest_framework import viewsets, permissions, mixins, status
from rest_framework.views import Response

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.profile)

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
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]

    def get_queryset(self):
        if self.action == "list":
            return Comment.objects.filter(owner__user=self.request.user)
        return Comment.objects.all()

    def perform_create(self, serializer):
        post_id = self.request.data.get("post")
        post = Post.objects.get_object_or_404(id=post_id)
        serializer.save(owner=self.request.user.profile, post=post)
