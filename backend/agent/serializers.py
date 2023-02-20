from rest_framework import serializers
from django.contrib.auth.models import User, Group

from .models import PropertyInspection
from landlord.serializers import PropertySerializer

class PropertyInspectionSerializer(serializers.HyperlinkedModelSerializer):
    property = PropertySerializer()

    class Meta:
        model = PropertyInspection
        fields = ['id', 'property', 'date_time']