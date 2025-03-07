from rest_framework import serializers

class PublicationSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField()
    text = serializers.CharField()
    pub_date_time = serializers.DateTimeField()
    likers = serializers.HyperlinkedRelatedField()

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField()
    text = serializers.CharField()
    pub_date_time = serializers.DateTimeField()
    likers = serializers.HyperlinkedRelatedField()
