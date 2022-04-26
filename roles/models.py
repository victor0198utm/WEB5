from django.db import models
from django.contrib.auth.models import User

# class User(AbstractUser):
#       EDITOR = 1
#       SUBSCRIBER = 2
      
#       ROLE_CHOICES = (
#           (EDITOR, 'Editor'),
#           (SUBSCRIBER, 'Subscriber'),
#       )
#       role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
#       want_to_edit = models.BooleanField(default=False)

# class Authorisation(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     is_editor = models.BooleanField(default=False)

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    is_editor = models.BooleanField(default=False)
    want_to_edit = models.BooleanField(default=False)