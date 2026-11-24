from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from .tokens import (
    generate_access_token,
    generate_refresh_token,
    validate_refresh_token,
)
from .models import Patient
from .serializer import (
    PatientSerializer,
    PatientRegistrationSerializer,
    PatientLoginSerializer,
    RefreshTokenSerializer
)
class PatientViewSet(ModelViewSet):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    @action(
        detail=False,
        methods=['post'],
        permission_classes=[AllowAny]
    )
    def register(self, request):

        serializer = PatientRegistrationSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        patient = serializer.save()

        return Response(
            {
                "message": "Patient registered successfully",
                "patient_id": patient.id,
                "name": patient.name,
                "email": patient.email
            },
            status=status.HTTP_201_CREATED
        )
    @action(
        detail=False,
        methods=['post'],
        permission_classes=[AllowAny],
        serializer_class=PatientLoginSerializer
    )
    def login(self, request):

        serializer = PatientLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = authenticate(
            username=email,
            password=password
        )

        if user is None:
            return Response(
                {"error": "Invalid email or password"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        access_token = generate_access_token(user)
        refresh_token = generate_refresh_token(user)

        return Response({
            "message": "Login successful",
            "access": access_token,
            "refresh": refresh_token
        })

    @action(
        detail=False,
        methods=['post'],
        permission_classes=[AllowAny],
        serializer_class=RefreshTokenSerializer
    )
    def refresh(self, request):

        serializer = RefreshTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        refresh_token = serializer.validated_data['refresh']

        payload = validate_refresh_token(refresh_token)

        if payload is None:
            return Response(
                {"error": "Invalid or expired refresh token"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        try:
            user = User.objects.get(id=payload['user_id'])
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        new_access_token = generate_access_token(user)

        return Response({
            "message": "Access token generated successfully",
            "access": new_access_token
        })