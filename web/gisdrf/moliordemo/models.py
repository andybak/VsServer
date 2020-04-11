# Django
from django.contrib.gis.db import models

# Managers
from .managers import BuildingManager

# Translation
from django.utils.translation import gettext_lazy as _


class Building(models.Model):

    name = models.CharField(max_length=100)
    outline = models.MultiPolygonField()
    height = models.FloatField()
    modified_at = models.DateTimeField(_('Modificado'), auto_now=True)
    created_at = models.DateTimeField(_('Creado'), auto_now_add=True)

    objects = BuildingManager()

    class Meta:
        verbose_name = _('Building')
        verbose_name_plural = _('Buildings')
        ordering = ['id']

    def __str__(self):
        return "{}".format(self.name)

    def getting_location(self):
        pass
