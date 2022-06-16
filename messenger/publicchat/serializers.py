from .models import *
from rest_framework import serializers


class PublicChatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PublicChat
        fields = ['name']

#class PublicMessageSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = PublicMessage
#        fields = ['author', 'chat', 'message', 'pub_date']
