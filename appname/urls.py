from django.urls import path
from .views import index,test,login,regspo,regus,spoboard,userboard
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',index,name='index'),
    path ('test/',test),
    path ('login/',login),
    path ('regspo/',regspo),
    path ('regus/',regus),
    path ('spoboard/',spoboard,name="sponsor_dashboard"),
    path ('userboard/',userboard,name="user_dashboard"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)