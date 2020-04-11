# Django REST Framework
from rest_framework.test import APITestCase
from rest_framework import status

# Models
from restaurants.models import Restaurant

# Utils
from django.shortcuts import reverse


class RestaurantAPITest(APITestCase):
    def setUp(self):
        url = reverse('api:restaurants_list')
        data = {'name': 'new restaurant',
            'twenty_four_hours': True,
            'address': "Avenida de las Flores, Murcia, España",
        }
        
        self.response = self.client.post(url, data, format='json')
        self.restaurant = Restaurant.objects.get(name="new restaurant")
        
        
    def test_can_create_new_restaurant(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_db_has_restaurants(self):
        self.assertGreater(Restaurant.objects.count(), 0)
    
    def test_db_has_object(self):
        self.assertTrue(Restaurant.objects.get(name="new restaurant"))

    def test_restaurant_has_pnt(self):
        self.assertTrue(self.restaurant.pnt)