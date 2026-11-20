
from django.db import models
from .mixins import TimeStampMixin
from django.contrib.auth.models import User

class Patient(TimeStampMixin):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    name = models.CharField(max_length=80)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name

