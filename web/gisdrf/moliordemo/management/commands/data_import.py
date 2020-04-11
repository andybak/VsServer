from pathlib import Path

from django.core.management.base import BaseCommand
import json
from django.contrib.gis.geos import fromstr, MultiPolygon, Polygon

from moliordemo.models import Building


class Command(BaseCommand):

    def handle(self, **options):

        Building.objects.all().delete()

        jsonfile = Path(__file__).parents[2] / "data.geojson"

        with open(str(jsonfile)) as datafile:

            objects = json.load(datafile)

            for obj in objects['features']:
                try:
                    objType = obj['geometry']['type']
                    if objType == 'Polygon':
                        name = str(int(obj['properties']['LDR.ID']))
                        coordinates = obj['geometry']['coordinates']
                        print ()
                        print (name)
                        # geo = fromstr(f'POLYGON({outlines})', srid=4326)
                        polys = []
                        for poly in coordinates:
                            poly = Polygon(poly, srid=27700)
                            poly.transform(4326)
                            polys.append(poly)
                        geo = MultiPolygon(polys)
                        b = Building(name=name, outline=geo)
                        b.save()
                except KeyError:
                    pass

