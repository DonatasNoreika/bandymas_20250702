from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

# Create your models here.
class CustomUser(AbstractUser):
    is_employee = models.BooleanField(verbose_name="Employee", default=True)

