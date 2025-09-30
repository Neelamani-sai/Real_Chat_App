from rest_framework import serializers
from .models import Message

class messageserializer(serializers.ModelSerializer):
    class meta:
        model = Message
        fields = ['id','user','text','timestamp']