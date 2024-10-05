from django import forms
from django.contrib.auth.models import User
from django.db import models
from .models import UserDetail,SponsorDetail

class userForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=['first_name','last_name','username','email','password'] 

class userAddForm(forms.ModelForm):
    class Meta():
        model=UserDetail
        fields=['umobile_no','uaddress','ulocation' ,'uphoto','description','no_year']

class sponsorForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=['first_name','last_name','username','email','password'] 

class sponsorAddForm(forms.ModelForm):
    class Meta():
        model=SponsorDetail
        fields=['smobile_no']

