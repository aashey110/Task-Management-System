from django.db import models
from customUser.models import CustomUser

# Create your models here.

    

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