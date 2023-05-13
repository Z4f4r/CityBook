from rest_framework import generics, mixins
from rest_framework.viewsets import GenericViewSet

from .models import Establishment
from .serializers import EstablishmentsSerializers, EstablishmentsInfoSerializers


class EstablishmentsViewSet(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            GenericViewSet):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentsInfoSerializers


class EstablishmentsAPIList(generics.ListAPIView):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentsSerializers
