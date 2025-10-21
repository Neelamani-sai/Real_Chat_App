from django.shortcuts import render
from .models import Message,profile,DirectMessage
from .serializers import messageserializer,Roomserializer,UserProfileSerializer
from rest_framework import generics,permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer,DirectMessageSerializer
from rest_framework.serializers import ModelSerializer
from rest_framework.permissions import AllowAny ,IsAuthenticated

# Create your views here.
class messageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all().order_by('-timestamp')
    serializers_class = messageserializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def chatroom(request):
    return render(request,'chat/chatroom.html') 

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self,serializer):
        user = serializer.save()
profile.objects.create(user=user)

def login_view(request):
    return render(request,'chat/login.html')
def register_view(request):
    return render(request,'chat/register.html')

class UserListCreateView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

class DirectMessageListCreateView(generics.ListCreateAPIView):
    serializer_class = DirectMessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return DirectMessage.objects.filter(sender=user) | DirectMessage.objects.filter(receiver=user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

class ProfileDetailUpdateView(generics.RetrieveUpdateAPIView):
    queryset = profile.objects.all()
    serializer_class = profileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile