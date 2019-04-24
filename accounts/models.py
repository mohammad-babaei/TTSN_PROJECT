from django.db import models
from django.contrib.auth.models import AbstractUser


class users (AbstractUser):
    username = models.CharField(max_length = 20,unique=True)
    password = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    joined_date = models.DateField(auto_now=True)
    projects = models.TextField(null=True)
    bio = models.TextField(null=True)

