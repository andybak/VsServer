import json

from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D
from django.template.response import TemplateResponse

from .models import Building


def index(request, lat, lng, distance):

    pnt = GEOSGeometry(f'POINT({lng} {lat})', srid=4326)
    buildings = Building.objects.filter(outline__distance_lte=(pnt, D(km=distance)))

    geojson = []
    print(buildings.count())

    for building in buildings:

        geojson.append (
            {
                "type": "Feature",
                "properties": {
                    "fid": "osgb5000005121014352",
                    "calculatedAreaValue": 85.156989,
                    "ldrid": building.name,
                    "AbsMin": 30.6,
                    "AbsH2": 39.5,
                    "AbsHMax": 40.2,
                    "RelH2": 8.9,
                    "RelHMax": 9.6
                },
                "geometry": json.loads(building.outline.geojson)
            }
        )

    context = {
        'lat': lat,
        'lng': lng,
        'buildings': buildings,
        'geojson': geojson
    }
    template = "molior/index.html"
    return TemplateResponse(request, template, context)


def building(request, ldrid):

    buildings = Building.objects.filter(name=ldrid);

    geojson = []

    for building in buildings:

        geojson.append (
            {
                "type": "Feature",
                "properties": {
                    "fid": "osgb5000005121014352",
                    "calculatedAreaValue": 85.156989,
                    "LDR.ID": 28481,
                    "AbsMin": 30.6,
                    "AbsH2": 39.5,
                    "AbsHMax": 40.2,
                    "RelH2": 8.9,
                    "RelHMax": 9.6
                },
                "geometry": json.loads(building.outline.geojson)
            }
        )

    context = {
        'buildings': buildings,
        'geojson': geojson
    }
    template = "molior/index.html"
    return TemplateResponse(request, template, context)