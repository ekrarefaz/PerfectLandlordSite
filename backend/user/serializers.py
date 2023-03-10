from rest_framework import serializers
from django.contrib.auth.models import User, Group

from .models import Profile

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups', 'first_name', 'last_name']

class UserFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'location', 'birth_date', 'get_image',
            'get_thumbnail', 'get_full_name']

class ProfileFormSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ['user_id', 'bio', 'location', 'birth_date']
        
    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user = User.objects.get(id=user_id)
        
        return Profile.objects.create(user=user, **validated_data)