from django.shortcuts import render
from .models import Patient
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import Patientserializer

@api_view(['GET'])
def patient_list(request):
    patients=Patient.objects.all()
    serializer=Patientserializer(patients,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def patient_created(request):
    serializer=Patientserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
            "message":"Patient created successfully",
            "data":serializer.data
            }, 
            status=status.HTTP_201_CREATED       
        )
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )
@api_view(['PUT'])
def patient_update(request,pk):
    try:
        patient=Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response(
            {
                "error":"Patient not found"},
                status=status.HTTP_404_NOT_FOUND
        )
    serializer=Patientserializer(patient,data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response({
            "message":"Patient Updated successfully",
            "data":serializer.data
        },
        status=status.HTTP_200_OK)
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST )

@api_view(['DELETE'])
def patient_delete(request,pk):
    try:
        patient=Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response({
            "error":"Patient not found"},
            status=status.HTTP_404_NOT_FOUND
            )
    patient.delete()
    return Response(
        {'message':'Patient deleted successfully'},
        status=status.HTTP_200_OK
    )