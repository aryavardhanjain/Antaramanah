from django.db import models
from accounts.models import User, UserProfile

# Create your models here.
class Therapist(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    user_profile = models.OneToOneField(UserProfile, related_name='userprofile', on_delete=models.CASCADE)
    therapist_name = models.CharField(max_length=50)
    amhs_id = models.CharField(max_length=100, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.amhs_id:
            self.amhs_id = f'amhs_{self.user.username}'
        
        first_name = self.user.first_name
        last_name = self.user.last_name

        self.therapist_name = f"{first_name} {last_name}"
        super().save(*args, **kwargs)
 
    def __str__(self):
        return self.therapist_name