# Django
from django.contrib.gis.db import models

# GeoDjango
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance


class BuildingManager(models.Manager):

    def get_buildings_near_pnt(self, x, y, results=None):

        queryset = self.annotate(
            distance=Distance('pnt', self.create_pnt(x, y))
            ).exclude(name__exact="no-name"
            ).order_by('distance')

        if results:
            return queryset[0:results]

        return queryset
        

    def create_pnt(self, x, y, srid=4326):
        return Point(float(x), float(y), srid=srid)