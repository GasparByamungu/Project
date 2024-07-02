from django import forms
from .models import Doctor


class ServiceForm(forms.Form):
    name = forms.CharField(max_length=100)
    contact = forms.CharField(max_length=100)
    medical_service = forms.ModelChoiceField(queryset=Doctor.objects.all())
