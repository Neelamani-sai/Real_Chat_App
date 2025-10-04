from django.urls import path
from .views import messageListCreateView,chatroom
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserListCreateView

urlpatterns = [
    path('messages/',messageListCreateView.as_view(), name = 'message_list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('',chatroom,name='message-list'),
]