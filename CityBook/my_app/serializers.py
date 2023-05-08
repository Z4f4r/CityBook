from rest_framework import serializers
from .models import Establishment


class EstablishmentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Establishment
        fields = ('title',)


class EstablishmentsInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Establishment
        fields = '__all__'
