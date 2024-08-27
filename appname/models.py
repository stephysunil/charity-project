from django.db import models

# Create your models here.
class UserDetail(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    mobile_no = models.BigIntegerField()
    location = models.CharField(max_length=50)
    photo = models.models.ImageField( upload_to="pics",blank=True,null=True)
    email = models.CharField(max_length=50)
    description = models.CharField( max_length=100)
    no_year = models.IntegerField()

class SponserDetail(models.Model):
        name = models.CharField(max_length=50)
        mobile_no = models.BigIntegerField()
        email = models.CharField(max_length=50)

class SponserShip(models.Model):
    amount = models.BigIntegerField()

class MedicalTeam(models.Model):
    member1name = models.CharField( max_length=50)
    member2name = models.CharField( max_length=50)
    mobile_no = models.BigIntegerField()
    email = models.CharField(max_length=50)

class Feedback(models.Model):
    name = models.CharField( max_length=50)
    mobile_no = models.BigIntegerField()
    email = models.CharField(max_length=50)
    message = models.CharField( max_length=50)
    


