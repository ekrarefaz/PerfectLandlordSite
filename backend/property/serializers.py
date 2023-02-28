from rest_framework import serializers

from .models import Property, SavedProperty

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            'id',
            'slug',
            'landlord_id',
            'type',
            'address',
            'get_absolute_url',
            'description',
            'price',
            'get_image',
            'get_thumbnail',
            'room',
            'bathroom',
            'furnished',
            'airConditioning',
            'pool',
            'gym',
        ]
    
    def create(self, validated_data):
        return Property.objects.create(**validated_data)
    
class SavedPropertySerializer(serializers.HyperlinkedModelSerializer):
    property = PropertySerializer()
    
    class Meta:
        model = SavedProperty
        fields = ['property']

    def create(self, validated_data):
        return SavedProperty.objects.create(**validated_data)
    
class SimplifiedSavedPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedProperty
        fields = ['property_id']

    def create(self, validated_data):
        return SavedProperty.objects.create(**validated_data)
     