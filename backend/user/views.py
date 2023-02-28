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

from .models import Profile
from .serializers import ProfileSerializer

class Signup(APIView):
    """
    Desc        : 

    Requires    : 
    - Authorization headers (Token),
    - Data:{
        "user": {
            "username": "landlord2",
            "password': "testest123456"
        },
        "bio": "halohalo ini landlord2"
    }

    Response    : A list of properties owned by user
    """
    def post(self, request, format=None):
        # Assign user to data
        serializer = ProfileSerializer(data=request.data)

        if serializer.is_valid():            
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MyProfile(APIView):
    """
    Desc        : Displays a list of all properties as long as user is logged in for tenants to browse
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    """
    Requires    : Authorization headers (token). Example: 
                    { 'Authorization' : 'Token    01ff9afdd60b6d23b92b5eed55dd87831a30bc9c' }
    Response    : User full profile with hyperlinked user object
    """

    def get(self, request, format=None):
        # Retrieve token
        tokenString = request.headers['Authorization'].split()[1]

        # Retrieve User
        token = Token.objects.get(key=tokenString)
        user = User.objects.get(username=token.user)

        # Retrieve profile of current user
        query = Profile.objects.get(user=user)
        serializer = ProfileSerializer(query)

        return Response(serializer.data)
    

class Tenants(APIView):
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

    def post(self, request, format=None):
        # Retrieve token
        tokenString = request.headers['Authorization'].split()[1]

        # Retrieve User
        token = Token.objects.get(key=tokenString)
        user = User.objects.get(username=token.user)

        # Retrieve all properties
        queryset = Property.objects.all()
        serializer = PropertySerializer(queryset, many=True)

        return Response(serializer.data)