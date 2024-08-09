from django.db import models

# Create your models here.
class userdetail(models.Model):
    name=models.CharField(max_length=50)
    address=models.models.CharField( max_length=50)
    mobile_no=models.models.BigIntegerField()
