from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User, PermissionsMixin

# Create your models here.
class User(auth.models.User, PermissionsMixin):
    def __str__(self):
        return f"@{username}"