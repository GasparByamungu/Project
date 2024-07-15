from django.contrib import admin
from.models import *


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['Name', 'mobile', 'special']

admin.site.register(Doctor, DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'mobile', 'address']

admin.site.register(Patient, PatientAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['Doctor', 'Patient', 'date', 'time']

admin.site.register(Appointment, AppointmentAdmin)

admin.site.register(Service)
admin.site.register(OtherService)

class PatientInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact', 'gender', 'adress', 'medical_service', 'other_service']

admin.site.register(PatientInfo, PatientInfoAdmin)