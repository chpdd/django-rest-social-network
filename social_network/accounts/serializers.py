from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Profile


# def create_hyplinkfield(app_name, view_names_list):
#     result = dict()
#     for view_name in view_names_list:
#         result[view_name] = serializers.HyperlinkedIdentityField(view_name=f"{app_name}:{view_name}-detail")
#     return result


# For some reason in HyperLinkedModelSerializer when creating a link by view_name, app_name is not taken into account
class ProfileSerializer(serializers.ModelSerializer):
    # locals().update(create_hyplinkfield('accounts', ['profile', 'user']))
    class Meta:
        model = Profile
        fields = ['birthday', 'bio']


class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='accounts:user-detail')
    profile = ProfileSerializer()
    class Meta:
        model = get_user_model()
        fields = ['url', 'username', 'email', 'profile']
