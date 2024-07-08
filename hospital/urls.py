
from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('service_form/', service_form_view, name='service_form'),
    path('patient_info', patient_info, name='patient_info'),
    path('view_appointment', view_appointment, name='view_appointment'),
]