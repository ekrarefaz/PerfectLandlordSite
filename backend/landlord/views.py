from django.contrib.auth.models import User, Group

from django.http import Http404
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import viewsets

from rest_framework import permissions
from rest_framework.authtoken.models import Token

from .models import Property, Profile
from .serializers import PropertySerializer, UserSerializer, GroupSerializer, ProfileSerializer

class UserList(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupList(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class PropertiesListRestricted(APIView):
    """
    API endpoint that allows properties that belongs to the user to be viewed and edited.
    """

    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        # Retrieve token
        tokenString = request.headers['Authorization'].split()[1]

        # Retrieve User
        token = Token.objects.get(key=tokenString)
        user = User.objects.get(username=token.user)

        queryset = Property.objects.filter(landlord_id=user.id)
        serializer = PropertySerializer(queryset, many=True)

        return Response(serializer.data)
    
class PropertiesList(APIView):
    """
    API endpoint that allows all properties to be viewed.
    """

    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        queryset = Property.objects.all()
        serializer = PropertySerializer(queryset, many=True)

        return Response(serializer.data)

class PropertyDetails(APIView):
    def get_object(self, property_slug):
        try:
            return Property.objects.get(slug=property_slug)
        except Property.DoesNotExist:
            raise Http404
    
    def get(self, request, property_slug, format=None):
        property = self.get_object(property_slug)
        serializer = PropertySerializer(property)
        return Response(serializer.data)

class ProfileView(APIView):
    """
    API endpoint that allows all tenants to be viewed.
    """

    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):

        # Retrieve profile of current user
        query = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(query, context={'request': request})

        return Response(serializer.data)


class TenantProfilesList(APIView):
    """
    API endpoint that allows all tenants to be viewed.
    """

    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        # Retrieve tenant group
        tenantGroup = Group.objects.get(name='tenant')

        # Retrieve only tenants users
        query = User.objects.filter(groups=tenantGroup)
        serializer = UserSerializer(query, many=True, context={'request': request})
        tenants = serializer.data
        
        # Retrieve from database
        profileQuery = Profile.objects.filter(user__in=query)
        profileSerializer = ProfileSerializer(profileQuery, many=True, context={'request': request})

        return Response(profileSerializer.data)