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
        fields = ["url", "pk", "owner", "text", "pub_date_time", "likers"]
        extra_kwargs = {
            "post": {"read_only": True},
            "likers": {"read_only": True},
            # "owner": {"read_only": True},
        }

class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = OwnerSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ["url", "pk", "owner", "text", "pub_date_time", "likers"]
        extra_kwargs = {
            "likers": {"read_only": True},
            # "owner": {"read_only": True},
        }


# class PostWithCommentsSerializer(PostSerializer):
#     comments = CommentSerializer(many=True, read_only=True)
#     class Meta(PostSerializer.Meta):
#         fields = PostSerializer.Meta.fields + ["comments"]


