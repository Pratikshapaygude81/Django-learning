from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from patient.models import Patient
from patient.serializers import Patientserializer
# Create your views here.
class PatientAPIView(APIView):
    def get(self,request):
        patients=Patient.objects.all()
        serializer=Patientserializer(patients,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=Patientserializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request):
        patient_id=request.data.get('id')
        try:
            patient=Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            return Response({'error':'patient not found'},
                            status=status.HTTP_404_NOT_FOUND)
        serializer=Patientserializer(patient,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request):
        patient_id=request.query_params.get('id')
        try:
            patient=Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            return Response({'error':'patient not found'},
                            status=status.HTTP_404_NOT_FOUND)
        patient.delete()

        return Response({"message":"Patient deleted successfully"},status=status.HTTP_200_OK)