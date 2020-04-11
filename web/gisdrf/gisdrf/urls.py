# Django
from django.contrib.gis import admin
from django.urls import path, include
from django.conf import settings

# Language prefix
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [] 

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('moliordemo.urls'), name="molior"),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        
    ] + urlpatterns