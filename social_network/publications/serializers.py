from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField("publications:post-detail")

    class Meta:
        model = Post
        fields = "__all__"
        # extra_kwargs = {"likers": {"read_only": True}}



class CommentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField("publications:comment-detail")
    # owner = serializers.HyperlinkedRelatedField
    class Meta:
        model = Comment
        fields = "__all__"
        # extra_kwargs = {"likers": {"read_only": True}}

