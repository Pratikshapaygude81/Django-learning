from rest_framework import serializers
from .models import Provider

class Providerserializer(serializers.ModelSerializer):
    class Meta:
        model=Provider
        fields='__all__'