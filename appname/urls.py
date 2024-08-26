from django.urls import path
from .views import index,test,login,regspo,regus,spoboard,userboard

urlpatterns = [
    path('',index,name='index'),
    path ('test/',test),
    path ('login/',login),
    path ('regspo/',regspo),
    path ('regus/',regus),
    path ('spoboard/',spoboard),
    path ('userboard/',userboard),
]
