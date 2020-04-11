from django.contrib.gis import admin

# Models
from django.contrib.gis.db.models.functions import Area, Perimeter, NumGeometries, NumPoints
from django.contrib.humanize.templatetags.humanize import intword

from .models import Building


@admin.register(Building)
class BuildingAdmin(admin.OSMGeoAdmin):

    def display_area(self, obj):
        return obj.outline.area * 1000000
    display_area.admin_order_field = Area('outline')
    display_area.short_description = "Area"

    # def display_perimeter(self, obj):
    #     return obj.outline.perimeter
    # display_perimeter.admin_order_field = Perimeter('outline')
    # display_perimeter.short_description = "Perimeter"

    def display_numpoints(self, obj):
        return obj.outline.num_points
    display_numpoints.admin_order_field = NumPoints('outline')
    display_numpoints.short_description = "Points"

    def display_numgeom(self, obj):
        return obj.outline.num_geom
    display_numgeom.admin_order_field = NumGeometries('outline')
    display_numgeom.short_description = "Polys"

    list_display = ('name', 'display_area', 'display_numpoints', 'display_numgeom')
    search_fields = ('name',)

