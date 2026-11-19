from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from provider.models import Provider
from .serializers import Providerserializer
# Create your views here.
class ProviderAPIView(APIView):
    def get(self,request):
        provider=Provider.objects.all()
        serializer=Providerserializer(provider,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=Providerserializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request):
        provider_id=request.get('id')
        try:
            provider=Provider.objects.get(id=provider_id)
        except Provider.DoesNotExist:
            return Response({'error':'Provider not found'},status=status.HTTP_404_NOT_FOUND)
        serializer=Providerserializer(provider,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=statsus.HTTP_400_BAD_REQUEST)

    def delete(self,request):
        provider_id=request.query_params.get('id')
        try:
            provider=Provider.objects.get(id=provider_id)
        except Provider.DoesNotExist:
            return Response({'error':'Provider not found'},status=status.HTTP_404_NOT_FOUND)
        provider.delete()
        return Response({'message':"Provider deleted successfully"},status=status.HTTP_200_OK)
