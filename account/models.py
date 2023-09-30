from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

   email = models.EmailField('Email Address', blank=False, max_length=254)

   USERNAME_FIELD = 'username'
   EMAIL_FIELD = 'email'
   