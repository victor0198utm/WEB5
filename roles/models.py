from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    is_editor = models.BooleanField(default=False)
    want_to_edit = models.BooleanField(default=False)