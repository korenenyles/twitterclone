from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class TwitterUser(AbstractUser):
    display_name = models.CharField(max_length=50, unique=True)

    
