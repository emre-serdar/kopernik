from django.shortcuts import render
from rest_framework import generics

from .serializers import SatelliteSerializer
from .models import Satellite

# Create your views here.

def renderUI(request):
    return render(request, 'satellite/index.html')
    
# satellite/list
class SatelliteListAPI(generics.ListAPIView):
    serializer_class = SatelliteSerializer
    queryset = Satellite.objects.all().order_by('-timeStamp') #order all satellites by creation time
    #to filter fetching according to satelliteID
    def get_queryset(self):
        queryset = super().get_queryset()
        satellite_id = self.request.query_params.get('satelliteID', None)
        if satellite_id is not None:
            queryset = queryset.filter(satelliteID=satellite_id)
        return queryset
# satellite/create
class SatelliteCreateAPI(generics.CreateAPIView):
        serializer_class = SatelliteSerializer
#to get last 7 satellite images in Today folder
# satellite/last-seven-satellite
class LastSevenSatellitesAPI(generics.ListAPIView):
    serializer_class = SatelliteSerializer
    queryset = Satellite.objects.all().order_by('-timeStamp')[:7]