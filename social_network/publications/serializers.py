from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='publications:post-detail')
    author = serializers.HyperlinkedRelatedField(view_name='accounts:user-detail', read_only=True)
    like_users = serializers.HyperlinkedRelatedField(many=True, view_name='accounts:user-detail', read_only=True)
    comments = serializers.HyperlinkedRelatedField(many=True, view_name='publications:comment-detail', read_only=True)

    class Meta:
        model = Post
        fields = ['url', 'author', 'text', 'pub_date', 'like_users', 'comments']
        read_only_fields = ['like_users', 'pub_date', 'comments']

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)


# class PostSerializer(serializers.ModelSerializer):
#     # like_users = serializers.Hyperlinked
#     # comments = serializers.HyperlinkedRelatedField(many=True, view_name='publications:comment-detail', read_only=True)
#     url = serializers.HyperlinkedIdentityField(view_name='publications:post-detail')
#     author = serializers.HyperlinkedRelatedField(view_name='accounts:user-detail',
#                                                  queryset=get_user_model().objects.all())
#     like_users = serializers.HyperlinkedRelatedField(many=True, view_name='accounts:user-detail',
#                                                      queryset=get_user_model().objects.all())
#     comments = serializers.HyperlinkedRelatedField(many=True, view_name='publications:comment-detail',
#                                                    queryset=Comment.objects.all())
#
#     class Meta:
#         model = Post
#         fields = ['url', 'author', 'text', 'pub_date', 'like_users', 'comments']
#         read_only_fields = ['author', 'like_users', 'pub_date', 'comments']


# class PostSerializer(serializers.ModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name='publications:post-detail')
#     author = serializers.CurrentUserDefault()
#     like_users = serializers.CreateOnlyDefault(None)
#     comments = serializers.CreateOnlyDefault(None)
#
#     class Meta:
#         model = Post
#         fields = ['url', 'author', 'text', 'pub_date', 'like_users', 'comments']


class CommentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='publications:comment-detail')
    post = serializers.HyperlinkedRelatedField(view_name='publications:post-detail', read_only=True)
    author = serializers.HyperlinkedRelatedField(view_name='accounts:user-detail', read_only=True)
    like_users = serializers.HyperlinkedRelatedField(many=True, view_name='accounts:user-detail', read_only=True)

    class Meta:
        model = Comment
        fields = ['url', 'post', 'author', 'text', 'pub_date', 'like_users']
        read_only_fields = ['post', 'author', 'pub_date', 'like_users']

    def create(self, validated_data):
        post = self.context['view'].kwargs.get('post_ok')
        validated_data['post'] = Post.objects.get(pk=post)
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)


# class CommentSerializer(serializers.ModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name='publications:post-detail')
#     post = serializers.URLField()
#     author = serializers.CurrentUserDefault()
#     like_users = serializers.CreateOnlyDefault(None)
#     comments = serializers.CreateOnlyDefault(None)
#
#     class Meta:
#         model = Comment
#         fields = ['url', 'post', 'author', 'text', 'pub_date', 'like_users', 'comments']
