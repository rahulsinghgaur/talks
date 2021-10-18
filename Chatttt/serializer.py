from rest_framework import serializers
from .models import Messages,Friend

class MessageSerializer(serializers.Serializer):
    key = serializers.CharField(max_length =100)
    sender = serializers.CharField(max_length = 100)
    receiver = serializers.CharField(max_length = 100)
    message = serializers.CharField()
    timestamp = serializers.CharField()

    def create(self,validate_data):
        return Messages.objects.create(**validate_data)

class FriendSerializer(serializers.Serializer):
    username= serializers.CharField(max_length=100)
    friends = serializers.CharField()     

    def create(self,validate_data):
        return Friend.objects.create(**validate_data)              