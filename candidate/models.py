from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    USER_TYPES = [
        ('investor', 'Investor'),
        ('innovator', 'Innovator'),
    ]

    name = models.CharField(max_length=255)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    
    # Add unique related_name for groups and user_permissions
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_user')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_user')

class Idea(models.Model):
    idea_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    idea_subject = models.CharField(max_length=255)
    idea_description = models.TextField()
    amount_expecting = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.idea_name