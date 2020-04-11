# Django
from django.urls import path, include

# Routers
from rest_framework.routers import DefaultRouter

# API Viewsets
from .apiviews import (RestaurantListView,
    PersonListView)


app_name = "api"

# router = DefaultRouter()
# router.register('v1/restaurants', RestaurantListView, basename='restaurants')


urlpatterns = [
    path('v1/restaurants/', RestaurantListView.as_view(), name='restaurants_list'),
    path('v1/persons/', PersonListView.as_view(), name='persons_list'),
] 

# urlpatterns += router.urls