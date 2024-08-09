from django.urls import path
from .views import index,demo

urlpatterns = [
    path('',index,name='index'),
    path ('test/',demo),
]
