import re

from django.urls import path, re_path, register_converter, converters
from .views import index


app_name = "vsserver"


urlpatterns = [
    path(f'', index, name='index'),
]