from django.contrib import admin
from appname.models import UserDetail,SponsorDetail,SponsorShip,MedicalTeam,Feedback

# Register your models here.
admin.site.register(UserDetail)
admin.site.register(SponsorDetail)
admin.site.register(SponsorShip)
admin.site.register(MedicalTeam)
admin.site.register(Feedback)
