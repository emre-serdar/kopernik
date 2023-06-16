from rest_framework import serializers
from .models import Satellite


class SatelliteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Satellite
        fields = [
            'get_image',
            'satelliteID',
            'timeStamp',
            'image',
            'title',
        ]
        extra_kwargs = {'timeStamp': {'read_only': True},
                        'get_image': {'read_only': True},
                        'image': {'write_only': True}, }
        # read_only => Only appears on GET requests.
        # write_only => Only appears on POST requests.