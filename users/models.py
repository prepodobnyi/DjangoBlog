from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    favorit_anime = models.CharField(max_length=100)

# Create your models here.
