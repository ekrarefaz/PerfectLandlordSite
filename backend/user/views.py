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
from .serializers import ProfileSerializer, ProfileFormSerializer

class Signup(APIView):
    """
    Desc        : 

    Requires    : 
    - Authorization headers (Token),
    - Data:{
        "user": {
            "username": "landlord2",
            "password": "testest123456"
        },
        "bio": "halohalo ini landlord2"
    }

    Response    : A list of properties owned by user
    """
    def post(self, request, format=None):
        # Retrieve user data
        user_data = request.data['user']
        user = User.objects.create(**user_data)

        # Retrieve group
        role = request.data['role']

        # Add user to group
        group = Group.objects.get(name=role)
        group.user_set.add(user)

        # Assign user to data
        serializer = ProfileFormSerializer(data=request.data)

        if serializer.is_valid():            
            serializer.save(user_id=user.id)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MyProfile(APIView):
    """
    Desc        : Displays the details of a user
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
    Desc        : Displays a list of all tenants as long as user is logged in
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    """
    Requires    : Authorization headers (token). Example: 
                    { 'Authorization' : 'Token    01ff9afdd60b6d23b92b5eed55dd87831a30bc9c' }
    Response    : List of all tenants in db
    """
    
    def get(self, request, format=None):
        # Retrieve token
        tokenString = request.headers['Authorization'].split()[1]

        # Retrieve group
        token = Token.objects.get(key=tokenString)
        group = Group.objects.get(name="Tenant")

        # Retrieve profiles
        profiles = Profile.objects.filter(user__groups=group)
        serializer = ProfileSerializer(profiles, many=True)

        return Response(serializer.data)