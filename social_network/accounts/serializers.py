from rest_framework import serializers

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField()
    birthday = serializers.DateField()
    bio = serializers.CharField()
