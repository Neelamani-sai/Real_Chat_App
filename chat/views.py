from django.shortcuts import render
from .models import Message
from .serializers import messageserializer
from rest_framework import generics
from django.contrib.auth.models import User

# Create your views here.
class messageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all().order_by('-timestamp')
    serializers_class = messageserializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer