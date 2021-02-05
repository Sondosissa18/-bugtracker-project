from django.db import models

from django.contrib.auth.models import AbstractUser


# from django.contrib.auth.models import User
from django.utils import timezone  

class MyUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

class Ticket(models.Model):

    STATUS_CHOICES = [
        ('done', 'Done'),
        ('new', 'New'),
        ('in progress', 'In Progress'),
        ('invalid', 'Invalid'),
    ]

    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    author = models.ForeignKey(MyUser, related_name='tickets', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="assigned_to", null=True)
    user_completed_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="user_completed_by", null=True)
    ticket_age = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")


    def __str__(self): 
        return f"{self.title} - {self.author}"
