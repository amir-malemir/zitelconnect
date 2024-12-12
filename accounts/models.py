from django.db import models
from django.contrib.auth.models import AbstractUser




class CustomUser(AbstractUser):
    phone_number = models.IntegerField(null=True, blank=True)
    is_admin = models.BooleanField(default=False)
