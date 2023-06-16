import os
from django.db import models
from django.conf import settings
from datetime import datetime, timedelta
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.contrib.sites.models import Site
import logging

# Create your models here.

class Satellite(models.Model):
    # Satellite Image infomation
    SATALLITE_TYPE_CHOICES = [
        ('15', 'NOAA 15'),
        ('18', 'NOAA 18'),
        ('19', 'NOAA 19'),
    ]
    # image = models.URLField(max_length=500) # Image by URL
    image = models.ImageField(blank=False, null=False,
                              upload_to='satellite/')  # Image by uploading
    satelliteID = models.CharField(
        max_length=2,
        choices=SATALLITE_TYPE_CHOICES,
        default='15',
        blank=False,
        null=False,
    )
    #image title
    title = models.CharField(max_length=255, blank=True, null=True)
    # Image time stamp.
    # auto_now_add=True: takes the instant datetime when a satellite obj is created
    timeStamp = models.DateTimeField(auto_now_add=True)

    # Creates image path. As: localhost:8000/[image_url]
    def get_image(self):
        if self.image:
            return Site.objects.get_current().domain + self.image.url
        else:
            return ""

    def get_image_path(self):
        if self.image:
            return os.path.join(settings.MEDIA_ROOT, self.image.name)
        else:
            return ""
    
    # Define display name of an object in the Django admin site.
    def __str__(self):
        return f'{self.get_satelliteID_display()} ({self.timeStamp})'


# function to delete old satellite objects and their corresponding images
def delete_old_satellites():
    seven_days_ago = datetime.now() - timedelta(days=7)
    old_satellites = Satellite.objects.filter(timeStamp__lt=seven_days_ago)
    for satellite in old_satellites:
        image_path = satellite.image.path
        if os.path.exists(image_path):
            os.remove(image_path)
        satellite.delete()

# delete old satellites and their images every day at midnight
@receiver(post_save, sender=Satellite)
def schedule_satellite_cleanup(sender, **kwargs):
    delete_old_satellites()

@receiver(pre_delete, sender=Satellite)
def delete_satellite_image(sender, instance, **kwargs):
    logger = logging.getLogger(__name__)
    # delete the image associated with the satellite object
    if instance:
        image_path = instance.get_image()
        if os.path.exists(image_path):
            os.remove(image_path)