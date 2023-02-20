import json
from rest_framework.views import APIView
from rest_framework import viewsets

from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

from .models import PropertyInspection
from .serializers import PropertyInspectionSerializer

from landlord.models import Property
from landlord.serializers import PropertySerializer

class InspectionsList(viewsets.ModelViewSet):

    queryset = PropertyInspection.objects.all()
    serializer_class = PropertyInspectionSerializer
    # permission_classes = [permissions.IsAuthenticated]

class PropertyInspectionList(APIView):

    def get_property(self, property_slug):
        try:
            return Property.objects.get(slug=property_slug)
        except Property.DoesNotExist:
            raise Http404
    
    def get(self, request, property_slug, format=None):
        property = self.get_property(property_slug)
        inspections = PropertyInspection.objects.filter(property=property)
        serializer = PropertyInspectionSerializer(inspections, many=True)
        return Response(serializer.data)
    