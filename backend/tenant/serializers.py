from rest_framework import serializers

from .models import SavedProperty
from landlord.serializers import PropertySerializer, UserSerializer

class SavedPropertySerializer(serializers.HyperlinkedModelSerializer):
    property = PropertySerializer()
    
    class Meta:
        model = SavedProperty
        fields = ['property']