# Django Rest Framework

# GeoDjango
from django.contrib.gis.geos import GEOSGeometry, Point

# APIViews
from rest_framework import generics

# Models
from restaurants.models import Restaurant
from persons.models import Person

# Serializers
from .serializers import RestaurantSerializer, PersonSerializer


class RestaurantListView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all().exclude(name__exact="no-name")
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        """
        Reformulamos el queryset en caso de recibir las cordenadas
        del usuario en la petición, la usaremos para devolver
        los restaurantes más cercanos a la cordenada indicada.
        """
        queryset = super().get_queryset()
        latitude = self.request.query_params.get('lat', None)
        longitude = self.request.query_params.get('lng', None)

        if latitude and longitude:
            queryset = Restaurant.objects.get_restaurants_near_pnt(
                                    longitude, latitude)

        return queryset


class PersonListView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def perform_create(self, serializer):
        """
        Validamos el formato de las cordenadas introducidas.
        """
        pnt_location = serializer.initial_data['pnt']

        # Separamos los valores introducidos por el usuario
        location = pnt_location.split(' ')
        pnt = Point(float(location[0]), float(location[1]))

        serializer.save(pnt=pnt)
