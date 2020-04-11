# Django
from django import template

register = template.Library()


@register.filter()
def distance_format(value):
    """
    Formateamos la distancia en metros obtenida por
    defecto con tal de mostrar una distancia más 
    amigable...
    """
    # import pdb; pdb.set_trace()
    if value.m <= 2000.00:
        return "{0:.2f} m".format(value.m)

    elif value.m > 2000.00:
        km = value.m / 1000.00
        return "{0:.3f} km".format(km)
