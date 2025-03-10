from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]
        extra_kwargs = {"username": {"read_only": True}}


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    url = serializers.HyperlinkedIdentityField("accounts:profile-detail")

    class Meta:
        model = Profile
        fields = "__all__"

    # def update(self, instance, validated_data):
    #     user_data = validated_data.pop("user", None)
    #     print("->\n" * 10, instance.user, "->\n" * 10)
    #     if user_data:
    #         for attr, value in user_data.items():
    #             setattr(instance.user, attr, value)
    #         instance.user.save()
    #     return super().update(instance, validated_data)

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", None)

        if user_data:
            user_serializer = UserSerializer(instance.user, data=user_data, partial=True)
            if user_serializer.is_valid(raise_exception=True):
                user_serializer.save()

        return super().update(instance, validated_data)  # Обновляем профиль
