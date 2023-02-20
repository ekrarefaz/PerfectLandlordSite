from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from rest_framework.response import Response

from django.contrib.auth.models import User, Group
from landlord.models import Property
from landlord.serializers import PropertySerializer

from rest_framework.authtoken.models import Token


class PropertiesList(APIView):
    """
    API endpoint that allows all available properties to be viewed
    """

    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        queryset = Property.objects.all()
        serializer = PropertySerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def search(request):

    # Retrieve query
    query = request.data.get('query', '')

    if query:
        properties = Property.objects.filter(Q(address__icontains=query))
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)
    else:
        return Response({"properties": []})

# Filter functionality 
@api_view(['POST'])
def filter(request):

    q_type = request.data.get(
        'type', 
        'Apartment,House,Townhouse,Studio,Retirement Home'
    ).split(',', -1)

    q_furnished = list(map(int, request.data.get(
        'furnished', 
        '0,1'
    ).split(',')))

    q_airConditioning = list(map(int, request.data.get(
        'airConditioning', 
        '0,1'
    ).split(',')))

    q_pool = list(map(int, request.data.get(
        'pool', 
        '0,1'
    ).split(',')))

    q_gym = list(map(int, request.data.get(
        'gym', 
        '0,1'
    ).split(',')))

    if q_type:
        properties = Property.objects.filter(
            type__in=q_type, 
            room__gte=int(request.data.get('minRoom', 0)), 
            room__lte=int(request.data.get('maxRoom', 1000)), 
            bathroom__gte=int(request.data.get('minBathroom', 0)), 
            bathroom__lte=int(request.data.get('maxBathroom', 1000)), 
            furnished__in=q_furnished,
            airConditioning__in=q_airConditioning,
            pool__in=q_pool,
            gym__in=q_gym,
        )        
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)
    else:
        return Response({"properties": []})