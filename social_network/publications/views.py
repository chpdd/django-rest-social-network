from rest_framework import response, viewsets, mixins, generics, permissions
from rest_framework.decorators import action


from .models import User, Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly & permissions.IsAuthenticated]


    @action(detail=True, methods=['post'])
    def create_comment(self, request, pk):
        data = request.data
        comment_serializer = CommentSerializer(data=data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return response.Response(comment_serializer)
        else:
            return response.Response()



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly & permissions.IsAuthenticated]

# class PublicationDetail(viewsets.ModelViewSet):
#     queryset = Publication.objects.all()
#     serializer_class = PublicationSerializer
