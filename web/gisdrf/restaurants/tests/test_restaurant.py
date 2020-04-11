# Django
from django.test import TestCase

# Models
from restaurants.models import Restaurant


class RestaurantTestCase(TestCase):
    def setUp(self):
        Restaurant.objects.create(name="Restaurante San Testeo")

    def test_db_has_restaurant(self):
        self.assertGreater(Restaurant.objects.all().count(), 0)
    
    def test_db_has_object(self):
        self.assertTrue(Restaurant.objects.get(name__exact="Restaurante San Testeo"))

