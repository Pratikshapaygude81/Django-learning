from django.db import models

# Create your models here.
class Patient(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    phone=models.CharField(max_length=15)
    email=models.EmailField(unique=True)
    address=models.CharField()
    Created_at=models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name