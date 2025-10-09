from rest_framework import serializers
from .models import Message,Room
from django.contrib.auth.models import User

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
