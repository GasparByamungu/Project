from django import forms
from .models import Service, OtherService, PatientInfo


class ServiceForm(forms.ModelForm):
    class Meta:
        model = PatientInfo
        fields = '__all__'

