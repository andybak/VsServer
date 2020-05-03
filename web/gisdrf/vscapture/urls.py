import re

from django.urls import include, path, re_path, register_converter, converters
from .views import index, chart_data
from django.conf import settings

app_name = "vsserver"


urlpatterns = [
    path(f'', index, name='index'),
    path('chart_data/<str:device>/<str:time_period>/', chart_data, name='chart_data'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns