# Models
from .models import Restaurant

# Utils


def generate_csv(x, y):
    """
    Creamos un archivo CSV con los restaurantes encontrados más 
    cercano a las cordenadas proporcionadas...
    """

    export = []

    # Cabecera del archivo CSV
    export.append([
        'ID',
        'Name',
        '24 Hrs',
        'Distance',
        'Location (x, y)',
    ])

    # Solicitamos los datos con los que crearemos el archivo CSV
    data = Restaurant.objects.get_restaurants_near_pnt(x, y, results=100)

    # Montamos una lista, que usaremos como fila en nuestro CSV File
    for result in data:
        yes_or_no = ["Yes!!" if result.twenty_four_hours else "No"]
        location = "%s %s" % (result.pnt.x, result.pnt.y)
        
        # Validamos el formato de la distancia a mostrarse
        if result.distance.m <= 1.000:
            distance = "{0:.2f} m".format(result.distance.m)
            
        elif result.distance.m > 1000:
            km = result.distance.m / 1000.00
            distance = "{0:.3f} km".format(km)

        # Guardamos la fila en nuestra lista 
        export.append([
            result.id,
            result.name.upper(),
            yes_or_no[0].upper(),
            distance,
            location,
        ])

    return export

