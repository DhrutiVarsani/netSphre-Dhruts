from django.db import models

# Create your models here.
class Alumni(models.Model):
    alumni_id = models.CharField(max_length = 50)
    name = models.CharField(max_length = 100)
    dob = models.DateField()
    blood_group = models.CharField(max_length = 10)
    gender = models.CharField(max_length = 10)
    last_login = models.DateTimeField()
    is_deleted = models.BooleanField()
    is_active = models.BooleanField()


class EduDetail(models.Model):
    edu_id = models.CharField(max_length = 50)
    user = models.ForeignKey(Alumni,on_delete = models.CASCADE)
    course = models.CharField(max_length = 100)
    specialization = models.CharField(max_length = 100)
    institute = models.CharField(max_length = 100)
    entry_date = models.DateField()
    passout_date = models.DateField()

class ProfessionalDetail(models.Model):
    prof_id = models.CharField(max_length = 50)
    alunmi = models.ForeignKey(Alumni,on_delete = models.CASCADE)
    orgname = models.CharField(max_length = 100)
    ocupation = models.CharField(max_length = 100)
    start_date = models.DateField()
    end_date = models.DateField()

class Connection(models.Model):
    conn_id = models.CharField(max_length = 50)
    follower = models.ForeignKey(Alumni,on_delete = models.CASCADE,related_name = 'follower')
    following = models.ForeignKey(Alumni,on_delete = models.CASCADE,related_name = 'following')
    since = models.DateTimeField()

class ConnectionRequest(models.Model):
    conn_req_id = models.CharField(max_length = 50)
    sender = models.ForeignKey(Alumni,on_delete = models.CASCADE,related_name = 'sender')
    receiver = models.ForeignKey(Alumni,on_delete = models.CASCADE,related_name = 'receiver')



