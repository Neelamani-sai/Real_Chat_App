from rest_framework import serializers
from .models import Message,Room
from django.contrib.auth.models import User
from .models import DirectMessage


class messageserializer(serializers.ModelSerializer):
    class meta:
        model = Message
        fields = ['id','user','text','timestamp']
class UserSerializer(serializers.ModelSerializer):
    class meta:
        model = User
        fields = ['id','username','email']
class Roomserializer(serializers.Modelserializer):
    class meta:
        model = Room
        fields = '__all__'
class UserProfileSerializer(serializers.ModelSerializer):
    serializers.ReadOnlyField(source='profile.is_online')
    class meta:
        model = User
        fields = ['id','username','is_online']
class DirectMessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.ReadOnlyField(source='sender.username')
    receiver_username = serializers.ReadOnlyField(source='receiver.username')

    class Meta:
        model = DirectMessage
        fields = ['id', 'sender', 'sender_username', 'receiver', 'receiver_username', 'message', 'timestamp']

