from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_description = models.TextField('Profile description', null=False, blank=True)

    def __str__(self):
        return self.profile_description

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'