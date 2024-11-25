from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')


    def __str__(self):
        return self.username
    

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    STATUS_CHOICE = (
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='not_started')
    assignto = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks')


    def __str__(self):
        return self.title