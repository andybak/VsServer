# Django
from django.contrib.gis import admin

# Models
from .models import Person

admin.site.register(Person, admin.OSMGeoAdmin)