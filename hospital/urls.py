
from django.urls import path
from .views import About, Home, Contact, Login, Logout_admin, Index, View_Doctor, Delete_Doctor, Add_Appointment, View_Appointment, Delete_Appointment, Add_Doctor, Add_Patient, View_Patient, Delete_Patient, service_form_view

urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('admin_login', Login, name='admin_login'),
    path('logout/', Logout_admin, name='logout_admin'),
    path('index/', Index, name='dashboard'),
    path('view_doctor/', View_Doctor, name='view_doctor'),
    path('view_appointment/', View_Appointment, name='view_appointment'),
    path('view_patient/', View_Patient, name='view_patient'),
    path('add_doctor/', Add_Doctor, name='add_doctor'),
    path('add_patient/', Add_Patient, name='add_patient'),
    path('add_appointment/', Add_Appointment, name='add_appointment'),
    path('delete_doctor(?P<int:pid)/', Delete_Doctor, name='delete_doctor'),
    path('delete_patient(?P<int:pid)/', Delete_Patient, name='delete_patient'),
    path('delete_appointment(?P<int:pid)/', Delete_Appointment, name='delete_appointment'),
    path('service_form/', service_form_view, name='service_form'),
]