from rest_framework import serializers
from django.contrib.auth.models import User, Group

from .models import Property


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            'id',
            'type',
            'address',
            'get_absolute_url',
            'description',
            'price',
            'get_image',
            'get_thumbnail'
        ]