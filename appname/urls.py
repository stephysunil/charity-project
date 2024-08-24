from django.urls import path
from .views import index,test,login

urlpatterns = [
    path('',index,name='index'),
    path ('test/',test),
    path ('login/',login),
]
