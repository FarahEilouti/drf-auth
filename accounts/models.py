from django.db import models
#
from django.contrib.auth.models import AbstractUser
#

# Create your models here.

# inherit abstract model
class CustomUser(AbstractUser):
    
    phone_number=models.CharField(max_length=20)