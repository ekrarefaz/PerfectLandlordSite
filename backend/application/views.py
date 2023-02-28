from django.db.models import Q
from django.contrib.auth.models import User, Group

from rest_framework.response import Response
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import viewsets

from rest_framework import permissions, authentication, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

from .models import *
from .serializers import *

class IdentityList(APIView):
    """
    Desc        : Displays application's identity item list
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    """
    Requires    : 
    - Authorization headers (token). 
    - Data: {
        application_id: 1
    }

    Response    : List of identity that has the application id
    """

    def post(self, request, format=None):
        # Retrieve application
        application_id = request.data["application_id"]
        application = Application.objects.get(id=application_id)

        # Retrieve all properties
        queryset = ApplicationIdentity.objects.filter(application=application)
        serializer = ApplicationIdentitySerializer(queryset, many=True)

        return Response(serializer.data)
    
class AddIdentity(APIView):
    """
    Desc        : Tenant to add identity proof item into the application
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    """
    Requires    : 
    - Authorization headers (token). 
    - Data: {
        'application_id': 1,
        'identity': {
            'item': 'Passport'
        }
    }

    Response    : Recently created identity item
    """

    def post(self, request, format=None):
        # Retrieve data
        application_id = request.data['application_id']

        # Create record of identity for application
        serializer = ApplicationIdentitySerializer(data=request.data)

        if serializer.is_valid():            
            serializer.save(application_id=application_id)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResidentialList(APIView):
    """
    Desc        : Displays application's residential item list
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    """
    Requires    : 
    - Authorization headers (token). 
    - Data: {
        application_id: 1
    }

    Response    : List of income that has the application id
    """

    def post(self, request, format=None):
        # Retrieve application
        application_id = request.data["application_id"]
        application = Application.objects.get(id=application_id)

        # Retrieve all properties
        queryset = ApplicationResidential.objects.filter(application=application)
        serializer = ApplicationResidentialSerializer(queryset, many=True)

        return Response(serializer.data)
    
class AddResidential(APIView):
    """
    Desc        : Tenant to add residential proof item into the application
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    """
    Requires    : 
    - Authorization headers (token). 
    - Data: {
        'application_id': 1,
        'residential': {
            'item': 'apartment'
        }
    }

    Response    : Recently created residential item
    """

    def post(self, request, format=None):
        # Retrieve data
        application_id = request.data['application_id']

        # Create record of residential for application
        serializer = ApplicationResidentialSerializer(data=request.data)

        if serializer.is_valid():            
            serializer.save(application_id=application_id)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmploymentList(APIView):
    """
    Desc        : Displays application's employment item list
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    """
    Requires    : 
    - Authorization headers (token). 
    - Data: {
        application_id: 1
    }

    Response    : List of employment that has the application id
    """

    def post(self, request, format=None):
        # Retrieve application
        application_id = request.data["application_id"]
        application = Application.objects.get(id=application_id)

        # Retrieve all properties
        queryset = ApplicationEmployment.objects.filter(application=application)
        serializer = ApplicationEmploymentSerializer(queryset, many=True)

        return Response(serializer.data)
    
class AddEmployment(APIView):
    """
    Desc        : Tenant to add employment proof item into the application
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    """
    Requires    : 
    - Authorization headers (token). 
    - Data: {
        'application_id': 1,
        'employment': {
            'item': 'cafe'
        }
    }

    Response    : Recently created employment item
    """

    def post(self, request, format=None):
        # Retrieve data
        application_id = request.data['application_id']

        # Create record of employment for application
        serializer = ApplicationEmploymentSerializer(data=request.data)

        if serializer.is_valid():            
            serializer.save(application_id=application_id)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IncomeList(APIView):
    """
    Desc        : Displays application's income item list
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    """
    Requires    : 
    - Authorization headers (token). 
    - Data: {
        application_id: 1
    }

    Response    : List of income that has the application id
    """

    def post(self, request, format=None):
        # Retrieve application
        application_id = request.data["application_id"]
        application = Application.objects.get(id=application_id)

        # Retrieve all properties
        queryset = ApplicationIncome.objects.filter(application=application)
        serializer = ApplicationIncomeSerializer(queryset, many=True)

        return Response(serializer.data)
    
class AddIncome(APIView):
    """
    Desc        : Tenant to add income proof item into the application
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    """
    Requires    : 
    - Authorization headers (token). 
    - Data: {
        'application_id': 1,
        'residential': {
            'item': 'apartment'
        }
    }

    Response    : Recently created income item
    """

    def post(self, request, format=None):
        # Retrieve data
        application_id = request.data['application_id']

        # Create record of residential for application
        serializer = ApplicationIncomeSerializer(data=request.data)

        if serializer.is_valid():            
            serializer.save(application_id=application_id)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubmitApplication(APIView):
    """
    Desc        : Tenant to submit an application to a property
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    """
    Requires    : 
    - Authorization headers (token). 
    - Data: {
        "property_id": 1,
        "cover_letter": "Hi this is me"
    }

    Response    : Recently created income item
    """

    def post(self, request, format=None):
        # Retrieve property
        property_id = request.data['property_id']

        # Retrieve token
        tokenString = request.headers['Authorization'].split()[1]

        # Retrieve User
        token = Token.objects.get(key=tokenString)
        user = User.objects.get(username=token.user) 

        # Create record of residential for application
        serializer = ApplicationFormSerializer(data=request.data)

        if serializer.is_valid():            
            serializer.save(tenant_id=user.id, property_id=property_id)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)