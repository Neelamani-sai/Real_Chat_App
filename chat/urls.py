from django.urls import path
from .views import messageListCreateView,chatroom
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserListCreateView
from .auth_views import RegisterView


urlpatterns = [
    path('messages/',messageListCreateView.as_view(), name = 'message_list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('',chatroom,name='chatroom'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/')
]