from django.db import models

# Create your models here.
class UserDetail(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    mobile_no = models.BigIntegerField()