from django import forms
from django.contrib auth.models import User 
from django.db import auth.models
from .models import UserDetail,SponsorDetail

class userForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        models=User
        fields=['first_name','last_name','username','email','password'] 

class userAddForm(forms.ModelForm):
    class Meta():
        models=UserDetail
        fields=['umobile_no','uaddress','uloctaion','uphoto','description','no_year']

class sponsorForm():
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        models=User
        fields=['first_name','last_name','username','email','password'] 

class sponsorAddForm(forms.ModelForm):
    class Meta():
        models=SponsorDetail
        fields=['smobile_no']