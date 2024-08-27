from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserDetail(models.Model):
    patient=models.OneToOneField(User,on_delete=models.CASCADE)
    is_patient=models.BooleanField(default=True)
    uname = models.CharField(max_length=50,null=True)
    uaddress = models.CharField(max_length=50,null=True)
    umobile_no = models.BigIntegerField(null=True)
    ulocation = models.CharField(max_length=50,null=True)
    uphoto = models.ImageField( upload_to="pics",blank=True,null=True)
    email = models.CharField(max_length=50,null=True)
    description = models.CharField( max_length=100)
    no_year = models.IntegerField()

    # def __str__(self):
    #     return self.uname

class SponsorDetail(models.Model):
        sponsor=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
        is_patient=models.BooleanField(default=False)

        sname = models.CharField(max_length=50,null=True)
        smobile_no = models.BigIntegerField(null=True)
        semail = models.CharField(max_length=50,null=True)

        # def __str__(self):
        #     return self.sname


class SponsorShip(models.Model):
    sname= models.CharField(max_length=50,null=True)
    uname= models.CharField(max_length=50,null=True)
    uaddress= models.CharField(max_length=50,null=True)
    umobile_no= models.BigIntegerField(null=True)
    ulocation= models.CharField(max_length=50,null=True)
    uphoto= models.ImageField( upload_to="pics",blank=True,null=True)
    smobile_no= models.BigIntegerField(null=True)
    semail= models.CharField(max_length=50,null=True)
    amount = models.BigIntegerField()

    # def __str__(self):
    #     return self.sname

class MedicalTeam(models.Model):
    member1name = models.CharField( max_length=50)
    member2name = models.CharField( max_length=50)
    mobile_no = models.BigIntegerField()
    email = models.CharField(max_length=50)

class Feedback(models.Model):
    uname = models.CharField( max_length=50)
    mobile_no = models.BigIntegerField()
    email = models.CharField(max_length=50)
    message = models.CharField( max_length=50)

    # def __str__(self):
    #     return self.uname
    


