from django.urls import path
from .views import messageListCreateView

urlpatterns = [
    path('messages/',messageListCreateView.as_view(), name = 'message_list'),
]