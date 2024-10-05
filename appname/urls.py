from django.urls import path
from .views import index,feed,login,regspo,regus,spoboard,userboard,pay,logout,seefeed
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',index,name='index'),
    path ('feed/',feed,name ="feed"),
    path ('seefeed/',seefeed,name="seefeed"),
    path ('login/',login,name="login"),
    path ('logout/',logout, name="logout"),
    path ('regspo/',regspo, name="registers"),
    path ('regus/',regus, name="registeru"),
    path ('pay/<str:patient>/<str:uaddress>/<int:umobile_no>/<str:ulocation>/<str:description>/<int:no_year>',pay,name="pay"),
    path('spoboard/',spoboard,name="sponsor_dashboard"),
    path ('userboard/',userboard,name="user_dashboard"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)