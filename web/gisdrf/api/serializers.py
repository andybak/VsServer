# Django DRF
from rest_framework import serializers

# Models
from restaurants.models import Restaurant
from persons.models import Person


class RestaurantSerializer(serializers.ModelSerializer):
    distance_km = serializers.DecimalField(source='distance.km', max_digits=10,
                                        decimal_places=3, required=False, read_only=True)

    distance_m = serializers.DecimalField(source='distance.m', max_digits=10,
                                    decimal_places=2, required=False, read_only=True)

    class Meta:
        model = Restaurant

        fields = ('id', 'name', 'address', 'pnt',
        'twenty_four_hours', 'distance_km', 'distance_m')

        read_only_fields = ('pnt',)


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        # fields = ('id', 'first_name', 'last_name', 'location', 'address')
        fields = '__all__'
        read_only_fields = ('address',)