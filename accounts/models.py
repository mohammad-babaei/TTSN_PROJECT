from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser


class users (AbstractUser):
    username = models.CharField(max_length = 20,unique=True)
    password = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    joined_date = models.DateField(auto_now=True)
    projects = models.TextField(null=True)
    bio = models.TextField(null=True)
    # profile_pic = models.FileField(upload_to="profile_pics/%Y/%m/%d/", max_length=100,blank=True,null=False)
    profile_picture = models.ImageField(default = "profile_pics/profile-default-male.png", upload_to="profile_pics/%Y/%m/%d/", height_field=None, width_field=None, max_length=None,null=False)

