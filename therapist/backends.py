from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import Therapist

class AMHSIDBackend(ModelBackend):
    def authenticate(self, request, amhs_id=None, password=None, **kwargs):
        try:
            therapist = Therapist.objects.get(amhs_id=amhs_id)
            user = therapist.user
        except Therapist.DoesNotExist:
            return None
        
        if user.check_password(password):
            return user
        return None