# Django
from django.contrib.gis.db import models

# Translation
from django.utils.translation import gettext as _


class Location(models.Model):
    """
        Clase abstracta de la cuál heredará todos los modelos que necesiten
        almacenar algún tipo de localización georeferencial.
    """
    address = models.CharField(_('Dirección'), max_length=100, null=True, blank=True)
    pnt = models.PointField(_('Punto de ubicación'), null=True, blank=True)

    modified_at = models.DateTimeField(_('Modificado'), auto_now=True)
    created_at = models.DateTimeField(_('Creado'), auto_now_add=True)

    class Meta:
        abstract=True