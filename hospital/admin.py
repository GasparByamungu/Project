from django.contrib import admin
from.models import *


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['Name', 'mobile', 'special']

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Service)
admin.site.register(OtherService)
admin.site.register(PatientInfo)