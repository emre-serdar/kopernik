import requests
import os
import time
from PIL import Image

# Function to send a POST request from Raspberry Pi to Django app on AWS
def post():
    directory = '/home/pi/weather/Today'
    url = 'https://django.emreserdar.com/satellite/create/'

    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        
        # Check if f is a file
        if os.path.isfile(f):
            # Check if file meets the conditions
            if filename.startswith('NOAA') and filename.endswith(".png") and "-map" not in filename:
               
                with Image.open(f) as img:
                    try:
                        # Extract information from image metadata
                        title = img.info['Satellite'] + " at " + img.info['Pass Start'] + " " + img.info['Enhancement']
                    except:
                        title = img.info['Satellite'] + " at " + img.info['Pass Start'] + " on " + img.info['Frequency'] + "MHz"
                
                satelliteID_index = filename.index('NOAA') + 4
                payload = {
                    "satelliteID": filename[satelliteID_index:satelliteID_index+2],
                    "title": title
                }

                # Open the image file in binary mode
                image = open(f, "rb")         
                print("Image to be uploaded:", filename)
                
                # Send the POST request with payload and image file
                response = requests.post(url, data=payload, files={"image": image})
                
                # Wait for 3 seconds
                time.sleep(3)
                
                # Check if the image was uploaded successfully
                if response.status_code == 201:
                    print("Image uploaded successfully")
                
                # Print the response text
                print("Response:", response.text)
                
                # Close the image file
                image.close()
                
                # Wait for 1 second before processing the next file
                time.sleep(1)

# Call the post() function to start the execution
post()
