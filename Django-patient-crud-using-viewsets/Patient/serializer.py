
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'


class PatientRegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = Patient
        fields = ['name', 'age', 'email', 'password']

    def create(self, validated_data):

        password = validated_data.pop('password')

        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=password
        )

        patient = Patient.objects.create(
            user=user,
            **validated_data
        )

        return patient
class PatientLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )