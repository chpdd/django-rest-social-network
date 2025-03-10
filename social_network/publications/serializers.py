from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        extra_kwargs = {
            "likers": {"read_only": True},
            "owner": {"read_only": True},
        }


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        extra_kwargs = {
            "post": {"read_only": True},
            "likers": {"read_only": True},
            "owner": {"read_only": True},
        }
