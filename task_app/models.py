from django.db import models


from customUser.models import CustomUser

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    STATUS_CHOICES = (
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('not_started', 'Not Started')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')
    assign_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks')



    def __str__(self):
        return self.title
    