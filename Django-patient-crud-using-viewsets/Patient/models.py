
from django.db import models
from .mixins import TimeStampMixin


class Patient(TimeStampMixin):

    name = models.CharField(max_length=80)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name

