from django.db import models

# Create your models here.
class School(models.Model):
    sid = models.CharField(max_length = 20)
    orgid = models.CharField(max_length = 20)
    name = models.CharField(max_length = 100)
    address = models.TextField(max_length = 300)
    is_deleted = models.BooleanField()

class SchoolRec(models.Model):
    recid = models.CharField(max_length = 50)
    user = models.CharField(max_length = 100)
    school = models.CharField(max_length = 100)
    entry_date = models.DateField()
    exit_date = models.DateField()
    entry_class = models.CharField(max_length = 20)
    passout_class = models.CharField(max_length = 20)

class Achievement(models.Model):
    achieve_id = models.CharField(max_length = 50)
    alumni = models.ForeignKey(SchoolRec, on_delete = models.CASCADE)
    achieve_date = models.DateField()
    achieve_desc = models.CharField(max_length = 100)
    cetrificate = models.FileField(upload_to = '')
    is_deleted = models.BooleanField()
    
    

    


    