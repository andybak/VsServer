from django.contrib.gis import admin

# Models
from .models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'pnt')
    search_fields = ('name',)