from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_student=models.BooleanField(default=False)

class studentlogin(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name='student',null=True)
    name=models.CharField(max_length=60)
    email=models.EmailField()
    rollnum=models.IntegerField(null=True,blank=True)
    collegename=models.CharField(max_length=100)
    phone=models.IntegerField(null=True,blank=True)
    status=models.IntegerField(default=0)

    def __str__(self):
         return self.name

class notificationadd(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
         return self.name

class StdntComplaint(models.Model):
    user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=200)
    complaint = models.TextField()
    date = models.DateField(auto_now=True)
    reply = models.TextField(null=True, blank=True)

    def __str__(self):
      return self.user