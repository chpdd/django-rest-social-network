from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Post, Comment
from accounts.models import Profile


class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Profile
        fields = ["url", "username"]


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = OwnerSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
        extra_kwargs = {
            "post": {"read_only": True},
            "likers": {"read_only": True},
            # "owner": {"read_only": True},
        }




class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = OwnerSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True, source="post_comments")

    class Meta:
        model = Post
        fields = "__all__"
        extra_kwargs = {
            "likers": {"read_only": True},
            # "owner": {"read_only": True},
        }
