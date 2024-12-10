from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('user', 'User')
    )
    role = models.CharField(max_length=10, choices=ROLES, default='user')

    def __str__(self):
        return self.username