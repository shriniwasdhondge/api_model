from django.db import models




class Response(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
    ]

    prompt = models.TextField()
    response_text = models.TextField()
    model_used = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    processing_time = models.FloatField()

    def __str__(self):
        return f"{self.prompt[:30]} - {self.model_used}"
# Create your models here.


from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
