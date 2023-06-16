from django.test import TestCase

# We have 2 ways to accomplish the goal..

# Option 1 - Example satellite image addition code

from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Satellite

image_path = "/Users/berkcohadar/Desktop/merwyn_project/Satellite-imagery-with-NWP-wind-and-thermal-advection-in-Visual-Weather.png"
image = SimpleUploadedFile(name='test_image.png', content=open(image_path, 'rb').read(), content_type='image/png')

satelliteID = '15'

Satellite(image = image, satelliteID = satelliteID).save()

# Option 2 - Create post request from the py file where we got the images. 

import requests
import json

headers = {'content-type': 'application/json'}
url = 'http://localhost:8080/satellite/create'

data = {"image": "IMAGE_PATH", "satelliteID": "15"}
params = {'token': '9ebbd0b25760557393a43064a92bae539d962103', 'format': 'xml', 'platformId': 1}

requests.post(url, params=params, data=json.dumps(data), headers=headers)