from django.urls import path, re_path
from .views import index, building


app_name = "molior"

urlpatterns = [
    re_path(r'(?P<lat>[-+]?[0-9]*\.?[0-9]+),(?P<lng>[-+]?[0-9]*\.?[0-9]+),(?P<distance>\d+)/$', index, name='index'),
    path('<int:ldrid>', building, name='building'),
]