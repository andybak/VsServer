# Django
from django.contrib.gis.db import models
from django.conf import settings

# Signals
from django.dispatch import receiver
from django.db.models.signals import pre_save

# Models
from locations.models import Location

# Utils
import geocoder


class Person(Location):
    """
    Heredamos de Location, el cuál tiene las siguientes propiedades:
        - address = models.CharField(max_length=100, null=True, blank=True)
        - pnt = models.PointField(null=True, blank=True)
        - modified_at = models.DateTimeField(auto_now=True)
        - created_at = models.DateTimeField(auto_now_add=True)
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)



# Signals

@receiver(pre_save, sender=Person)
def getting_address(sender, instance, **kwargs):
    """
    Obtenemos la dirección del individuo a partir de sus cordenadas,
    con la ayuda de la API Geocoding de Google.
    """

    if instance.pnt:
        pnt_location = instance.pnt

        # Convertimos el objeto de localización a una string para consultar la API
        location_string = "%s %s" % (pnt_location.x, pnt_location.y)

        # Solicitamos INFO a la API de Google
        g = geocoder.google(location_string, method='reverse', key=settings.GOOGLE_API_KEY)

        address = g.json.get('address')
        instance.address = address

