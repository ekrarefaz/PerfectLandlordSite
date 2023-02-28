from rest_framework import serializers
from django.contrib.auth.models import User, Group

from .models import *
from property.serializers import PropertySerializer
from user.serializers import UserSerializer

class IdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id', 'item']

class ResidentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id', 'item']

class EmploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id', 'item']

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id', 'item']

class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    property = PropertySerializer()
    tenant = UserSerializer()

    class Meta:
        model = Application
        fields = ['id', 'property', 'tenant', 'date_time', 'cover_letter']

class ApplicationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['property_id', 'tenant_id', 'cover_letter']

    def create(self, validated_data):
        return Application.objects.create(**validated_data)

class ApplicationIdentitySerializer(serializers.HyperlinkedModelSerializer):
    identity = IdentitySerializer()

    class Meta:
        model = ApplicationIdentity
        fields = ['id', 'application_id', 'identity']
    
    def create(self, validated_data):
        identity_data = validated_data.pop('identity')
        identity = Identity.objects.create(**identity_data)
        return ApplicationIdentity.objects.create(identity=identity,**validated_data)

class ApplicationResidentialSerializer(serializers.HyperlinkedModelSerializer):
    residential = ResidentialSerializer()

    class Meta:
        model = ApplicationResidential
        fields = ['id', 'application_id', 'residential']
    
    def create(self, validated_data):
        residential_data = validated_data.pop('residential')
        residential = Residential.objects.create(**residential_data)
        return ApplicationResidential.objects.create(residential=residential,**validated_data)

class ApplicationEmploymentSerializer(serializers.HyperlinkedModelSerializer):    
    employment = EmploymentSerializer()

    class Meta:
        model = ApplicationEmployment
        fields = ['id', 'application_id', 'employment']
    
    def create(self, validated_data):
        employment_data = validated_data.pop('employment')
        employment = Employment.objects.create(**employment_data)
        return ApplicationEmployment.objects.create(employment=employment,**validated_data)

class ApplicationIncomeSerializer(serializers.HyperlinkedModelSerializer):
    income = IncomeSerializer()

    class Meta:
        model = ApplicationIncome
        fields = ['id', 'application_id', 'income']
    
    def create(self, validated_data):
        income_data = validated_data.pop('income')
        income = Income.objects.create(**income_data)
        return ApplicationIncome.objects.create(income=income,**validated_data)