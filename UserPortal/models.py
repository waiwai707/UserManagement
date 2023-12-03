from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    email = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100)
    status = models.CharField(max_length=100,null=True)
