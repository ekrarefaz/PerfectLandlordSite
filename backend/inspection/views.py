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

from property.models import Property
from .models import PropertyInspection
from .serializers import PropertyInspectionSerializer, SimplifiedPropertyInspectionSerializer, InspectionRegistrationSerializer

class ViewInspection(APIView):
    """
    Desc        : View the inspection times available for a property
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    """
    Requires    : 
    - Authorization headers (token)
    - Data: {
        "property_id":1
    }
        
    Response    : List of available inspection times for a property
    """

    def get(self, request, format=None):
        # Retrieve Property
        property_id = request.data["property_id"]
        property = Property.objects.get(id=property_id)

        # Retrieve property inspection times
        queryset = PropertyInspection.objects.filter(property=property)
        serializer = PropertyInspectionSerializer(queryset, many=True)

        return Response(serializer.data)
    
class CreateInspection(APIView):
    """
    Desc        : Landlord to create inspection times for a specific property
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    """
    Requires    : 
    - Authorization headers (Token),
    - Data:{
        "property_id": 4,
        "date_time": "2006-10-25 14:30:59" 
    }

    Response    : The inspection time created
    """
    def post(self, request, format=None):

        # Retrieve property
        property_id = request.data["property_id"]

        # Create inspection time based on property_id and date_time
        serializer = SimplifiedPropertyInspectionSerializer(data=request.data)

        if serializer.is_valid():            
            serializer.save(property_id=property_id)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterInspection(APIView):
    """
    Desc        : Tenant to resgister to a property inspection tieme
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    """
    Requires    : 
    - Authorization headers (Token),
    - Data:{
        "inspection_id": 1
    }

    Response    : The inspection time registered
    """
    def post(self, request, format=None):
        # Retrieve inspection
        inspection_id = request.data["inspection_id"]  
        
        # Retrieve token
        tokenString = request.headers['Authorization'].split()[1]

        # Retrieve User
        token = Token.objects.get(key=tokenString)
        user = User.objects.get(username=token.user) 
        
        # Create inspection registration based on inspection_id
        serializer = InspectionRegistrationSerializer(data=request.data)

        if serializer.is_valid():            
            serializer.save(inspector_id=user.id, inspection_id=inspection_id)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)