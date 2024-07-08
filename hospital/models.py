
from django.db import models

# Create your models here.


class Doctor(models.Model):
    Name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    special = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)   
    address = models.TextField()

    def __str__(self):
        return self.name
    

class Appointment(models.Model):
    Doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    Patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()     

    def __str__(self):
        return self.Doctor.Name + "__"+self.Patient.name


class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    

class OtherService(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    

class PatientInfo(models.Model):
    name = models.CharField(max_length=150)
    contact = models.CharField(max_length=100)
    medical_service = models.ForeignKey(Service, on_delete=models.CASCADE)
    other_service = models.ForeignKey(OtherService, on_delete=models.CASCADE)
