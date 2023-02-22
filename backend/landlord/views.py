from django.db.models import Q
from django.contrib.auth.models import User, Group

from rest_framework.response import Response
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.decorators import api_view
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
    # permission_classes = [permissions.IsAuthenticated]

class PropertiesList(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    # permission_classes = [permissions.IsAuthenticated]

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

# Search functionality based on address
@api_view(['POST'])
def search(request):

    # Retrieve query
    query = request.data.get('query', '')

    # Retrieve User
    tokenString = request.headers['Authorization'].split()[1]
    token = Token.objects.get(key=tokenString)
    user = User.objects.get(username=token.user)

    if query:
        properties = Property.objects.filter(landlord_id=user.id)
        properties = properties.filter(Q(address__icontains=query))
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)
    else:
        return Response({"properties": []})


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
    API endpoint that user own profile to be viewed
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