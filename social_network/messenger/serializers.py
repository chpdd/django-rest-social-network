from rest_framework import serializers

from .models import Chat, GroupChat


class ChatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chat
        fields = "__all__"
        extra_kwargs = {
            "member1": {"read_only": True},
            "member2": {"read_only": True},
        }


class GroupChatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroupChat
        fields = "__all__"
        extra_kwargs = {
        }
