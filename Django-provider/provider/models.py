from django.db import models

# Create your models here.
class Provider(models.Model):
    doctor_name=models.CharField(max_length=100)
    doctor_age=models.PositiveIntegerField()
    doctor_email=models.EmailField(unique=True)
    doctor_phone=models.CharField(max_length=15)
    doctor_specialization=models.CharField(max_length=100)
    availability = models.DateTimeField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    Update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.doctor_name