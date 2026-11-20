
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

from .models import Patient
from .serializer import (
    PatientSerializer,
    PatientRegistrationSerializer
)
from .serializer import PatientLoginSerializer

class PatientViewSet(ModelViewSet):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    @action(detail=False, methods=['post'])
    def register(self, request):

        serializer = PatientRegistrationSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "message": "Patient registered successfully",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
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

        user = authenticate(username=email, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                "message": "Login successful",
                "token": token.key
              })

        return Response(
        {"error": "Invalid email or password"},
        status=status.HTTP_401_UNAUTHORIZED
    )