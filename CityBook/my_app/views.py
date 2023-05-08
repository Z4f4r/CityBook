from rest_framework import generics
from django.shortcuts import render, get_object_or_404
from .models import Establishment
from .serializers import EstablishmentsSerializers, EstablishmentsInfoSerializers


class EstablishmentsAPIList(generics.ListCreateAPIView):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentsSerializers


class EstablishmentsAPIInfo(generics.ListCreateAPIView):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentsInfoSerializers
