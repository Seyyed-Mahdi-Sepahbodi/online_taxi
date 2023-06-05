from django.db import models
from django.contrib.auth.models import AbstractUser # new

# Create your models here.

class User(AbstractUser):
    pass