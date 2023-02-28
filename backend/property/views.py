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

from .models import Property, SavedProperty
from .serializers import PropertySerializer, SavedPropertySerializer, SimplifiedSavedPropertySerializer

class Properties(APIView):
    """
    Desc        : Displays a list of all properties as long as user is logged in for tenants to browse
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    """
    Requires    : Authorization headers (token). Example: 
                    { 'Authorization' : 'Token    01ff9afdd60b6d23b92b5eed55dd87831a30bc9c' }
    Response    : List of all properties in db
    """

    def get(self, request, format=None):
        # Retrieve token
        tokenString = request.headers['Authorization'].split()[1]

        # Retrieve User
        token = Token.objects.get(key=tokenString)
        user = User.objects.get(username=token.user)

        # Retrieve all properties
        queryset = Property.objects.all()
        serializer = PropertySerializer(queryset, many=True)

        return Response(serializer.data)
    

class PropertyDetails(APIView):
    """
    Desc        : Displays athe details of a certain property
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    """
    Requires    : 
    - Header : Authorization Token 
    - Slug : Property id

    Response    : Property as a JSON object 
    { id, type, address, get_absolute_url, description, price, get_image, get_thumbnail, room, bathroom, furnished, air_conditioning, pool, gym}
    """
    def get_object(self, property_slug):
        try:
            return Property.objects.get(slug=property_slug)
        except Property.DoesNotExist:
            raise Http404
    
    def get(self, request, property_slug, format=None):
        property = self.get_object(property_slug)
        serializer = PropertySerializer(property)
        return Response(serializer.data)
    

class SavedProperties(APIView):
    """
    Desc        : Display a list of or add to properties saved by loged-in user (tenant) 
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    """
    Requires    : Authorization headers (token). 
    Response    : A list of properties saved by user
    """
    def get(self, request, format=None):
        # Retrieve token
        tokenString = request.headers['Authorization'].split()[1]

        # Retrieve User
        token = Token.objects.get(key=tokenString)
        user = User.objects.get(username=token.user)

        # Retrieve all properties
        queryset = SavedProperty.objects.filter(tenant=user)
        serializer = SavedPropertySerializer(queryset, many=True)

        return Response([p['property'] for p in serializer.data])

    """
    Requires    : 
    - Authorization headers (Token),
    - Data:{
        "property_id": 4
    }

    Response    : A list of properties owned by user
    """
    def post(self, request, format=None):
        # Retrieve token
        tokenString = request.headers['Authorization'].split()[1]

        # Retrieve User
        token = Token.objects.get(key=tokenString)
        user = User.objects.get(username=token.user)

        # Assign user to data
        property_id = request.data["property_id"]
        serializer = SimplifiedSavedPropertySerializer(data=request.data)

        if property_id and serializer.is_valid():            
            serializer.save(tenant_id=user.id, property_id=property_id)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    
class MyProperties(APIView):
    """
    Desc        : Display a list of or add to properties that belongs to the currently logged-in user (Landlord) 
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    """
    Requires    : Authorization headers (token). 
    Response    : A list of properties owned by user
    """
    def get(self, request, format=None):
        # Retrieve token
        tokenString = request.headers['Authorization'].split()[1]

        # Retrieve User
        token = Token.objects.get(key=tokenString)
        user = User.objects.get(username=token.user)

        # Retrieve all properties
        queryset = Property.objects.filter(landlord_id=user.id)
        serializer = PropertySerializer(queryset, many=True)

        return Response(serializer.data)

    """
    Requires    : 
    - Authorization headers (Token),
    - Data:{
        "slug": "32-rodwell-st",
        "type": "Apartment",
        "address": "32 Rodwell St",
        "description": "hello",
        "price": "200",
        "room": 1,
        "bathroom": 1,
        "furnished": 1,
        "airConditioning": 1,
        "pool": 1,
        "gym": 1
    }

    Response    : A list of properties owned by user
    """
    def post(self, request, format=None):
        # Retrieve token
        tokenString = request.headers['Authorization'].split()[1]

        # Retrieve User
        token = Token.objects.get(key=tokenString)
        user = User.objects.get(username=token.user)

        # Assign user to data
        serializer = PropertySerializer(data=request.data)

        if serializer.is_valid():            
            serializer.save(landlord_id=user.id)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class SearchProperties(APIView):
    """
    Desc        : Search through a list of properties with a certain query
    """

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    """
    Requires    : 
    - Authorization headers (Token)
    - Data:
    {
        "query": [ search query ],
        "filter": [ '', 'my-properties' ]
    }

    Response    : A list of properties owned by user
    """
    def post(self, request, format=None):
        # Retrieve data
        query = request.data.get('query', '')
        filter = request.data.get('filter', '')

        # Filter properties based on search query
        properties = Property.objects.filter(Q(address__icontains=query))
    
        # Implement extra filter
        if (filter == 'my-properties'):
            # Retrieve User
            tokenString = request.headers['Authorization'].split()[1]
            token = Token.objects.get(key=tokenString)
            user = User.objects.get(username=token.user)

            # Assign filter
            properties = properties.filter(landlord_id=user.id)
        
        # Serialize and return
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)

    

class FilterProperties(APIView):
    """
    Desc        : Filter properties based on user selections
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    """
    Requires    : 
    - Authorization headers (Token)
    - Data:
    {
        "filter": "my-properties",
        "selected": {
            "type": ["Apartment","House"],
            "furnished": [1],
            "minRoom": 0,
            "maxRoom": 1000,
            "minBathroom": 0,
            "maxBathroom": 1000,
            "pool": [1],
            "gym": [1]
    }

    Response    : List of properties that macth the filter
    """
    def post(self, request, format=None):
        # Define selectable fields
        selectFields = ['type', 'furnished', 'pool', 'airConditioning', 'gym']

        # Selection defaults
        selected = {
            "type": ['Apartment','House','Townhouse','Studio','Retirement Home'],
            "furnished": [0,1],
            "minRoom": 0,
            "maxRoom": 1000,
            "minBathroom": 0,
            "maxBathroom": 1000,
            "pool": [0,1],
            "airConditioning":[0,1],
            "gym": [0,1],
        }

        # Assign user selection to selected
        input = request.data.get('selected')
        if input:
            for i in input:
                if (i in selectFields):
                    selected[i] = request.data["selected"][i]

        # Filter properties based on selections
        properties = Property.objects.filter(
            type__in = selected["type"], 
            furnished__in = selected["furnished"],
            room__gte = selected["minRoom"], 
            room__lte = selected["maxRoom"], 
            bathroom__gte = selected["minBathroom"], 
            bathroom__lte = selected["maxBathroom"], 
            airConditioning__in = selected["airConditioning"],
            pool__in = selected["pool"],
            gym__in = selected["gym"],
        )     

        # Implement extra filter
        filter = request.data.get('filter', '')
        if (filter == 'my-properties'):
            # Retrieve User
            tokenString = request.headers['Authorization'].split()[1]
            token = Token.objects.get(key=tokenString)
            user = User.objects.get(username=token.user)

            # Assign filter
            properties = properties.filter(landlord_id=user.id)

        # Serialize and return
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)
