from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class USER_LOGIN(models.Model):
    first_name = models.CharField(max_length=35, blank=False)
    last_name = models.CharField(max_length=35, blank=False)
    user_name = models.CharField(max_length=35, blank=False, primary_key=True)
    email_id = models.EmailField(max_length=35, blank=False )
    pass_word = models.CharField(max_length=35, blank=False)
    gender=models.CharField(max_length=10,blank=False)

class USER_RESULT(models.Model):
    user=models.OneToOneField(USER_LOGIN,on_delete=models.CASCADE)
    result=models.CharField(max_length=10,blank=False)