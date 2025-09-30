from django.shortcuts import render
from .models import Message
from .serializers import messageserializer
from rest_framework import generics

# Create your views here.
class messageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all().order_by('-timestamp')
    serializers_class = messageserializer

