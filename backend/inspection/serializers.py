from rest_framework import serializers
from django.contrib.auth.models import User, Group

from .models import PropertyInspection, InspectionRegistration
from property.serializers import PropertySerializer

class PropertyInspectionSerializer(serializers.HyperlinkedModelSerializer):
    property = PropertySerializer()

    class Meta:
        model = PropertyInspection
        fields = ['id', 'property', 'date_time']

class SimplifiedPropertyInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyInspection
        fields = ['id', 'property_id', 'date_time']

    def create(self, validated_data):
        return PropertyInspection.objects.create(**validated_data)

class InspectionRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionRegistration
        fields = ['inspection_id']
    
    def create(self, validated_data):
        return InspectionRegistration.objects.create(**validated_data)