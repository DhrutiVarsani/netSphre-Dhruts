from django.db import models

# Create your models here.
class organisation(models.Model):
    orgid = models.CharField(max_length=20)
    name = models.CharField(max_length = 100)
    address = models.TextField(max_length = 200)
    is_deleted = models.BooleanField()


