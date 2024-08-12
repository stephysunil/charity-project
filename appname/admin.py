from django.contrib import admin
from appname.models import UserDetail,SponserDetail,SponserShip,MedicalTeam,Feedback

# Register your models here.
admin.site.register(UserDetail)
admin.site.register(SponserDetail)
admin.site.register(SponserShip)
admin.site.register(MedicalTeam)
admin.site.register(Feedback)
