from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user.username}:{self.text[:30]}"

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_seen = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return self.user.username

    @property
    def is_online(self):
        # If active within the last 2 minutes, mark as online
        return (timezone.now() - self.last_seen).total_seconds() < 120
class DirectMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return f"{self.sender} → {self.receiver}: {self.message[:20]}"
    