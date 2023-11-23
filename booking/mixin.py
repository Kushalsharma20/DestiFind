from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.mixins import AccessMixin

from auth_app import models as AuthModels

from django.contrib.sessions.models import Session
from django.utils import timezone

class SecuredAccessMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse("auth_app:login"))
        
        try:
            session = Session.objects.get(session_key=request.session.session_key)
            # Get the current time
            current_time = timezone.now()

            # Check if the session was created more than 10 minutes ago
            print(dir(session))
            print(session.expire_date)
            print(current_time)
            print(timezone.timedelta(minutes=10))

            if not True:
                return redirect(reverse("booking:verify_code"))
            
        except Session.DoesNotExist:
            # Session with the given key does not exist
            return redirect(reverse("auth_app:login"))
        
        # sendCode(request.user)
        return super().dispatch(request, *args, **kwargs)