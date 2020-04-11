# Django
from django.conf import settings

# Signals
from django.dispatch import receiver
from django.db.models.signals import pre_save

# Models
from .models import Restaurant

# Utils
import geocoder


# @receiver(pre_save, sender=Restaurant)
def getting_location_pnt(sender, instance, **kwargs):
    """
    Obtenemos la dirección introducida, la convertimos a
    cordenadas para después guardarla en la propiedad 'pnt'.
    """
    if not instance.address:
        return

    address = instance.address
    g = geocoder.google(address, key=settings.GOOGLE_API_KEY)
    latitude = g.json.get('lat')
    longitude = g.json.get('lng')
    
    
    pnt = sender.objects.create_pnt(longitude, latitude)

    if instance.pnt != pnt:
        instance.pnt = pnt