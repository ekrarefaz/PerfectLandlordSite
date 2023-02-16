from rest_framework import serializers
from django.contrib.auth.models import User, Group

from .models import Property, Profile


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups', 'first_name', 'last_name']

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'location', 'birth_date', 'get_image',
            'get_thumbnail', 'get_full_name']

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