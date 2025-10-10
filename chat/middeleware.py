from django.utils import timezone
from .models import profile

class UpdateLastSeenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        user = request.user
        if user.is_authenticated:
            profile.objects.filter(user=user).update(last_seen=timezone.now())
        return response