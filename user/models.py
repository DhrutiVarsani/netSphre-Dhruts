from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.CharField(max_length = 5)
    email = models.EmailField(max_length = 50)
    password = models.CharField(max_length = 50)
    userType = models.CharField(max_length = 20)