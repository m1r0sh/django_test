from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Post(models.Model):
    theme = models.CharField("theme", max_length=150)
    description = models.CharField("description", max_length=150)

    def __str__(self):
        return self.theme
    