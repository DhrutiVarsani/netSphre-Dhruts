from django.db import models

# Create your models here.
class Message(models.Model):
    message_id = models.CharField(max_length = 50)
    message = models.TextField()
    send = models.ForeignKey('alumni.Alumni',on_delete = models.CASCADE,related_name = 'send')
    receive = models.ForeignKey('alumni.Alumni',on_delete = models.CASCADE,related_name = 'receive')
    time = models.DateTimeField()
    is_deleted = models.BooleanField()