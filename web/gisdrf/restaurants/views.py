# Django
from django.shortcuts import render, redirect
from django.views import View

# GeoDjango
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance

# Models
from .models import Restaurant

# Utils
import django_excel as excel
from django.utils import timezone

# Tasks
from .tasks import show_hello_world
from .generate_csv import generate_csv


# Example view that will get real-time events on the client

from django.views import generic
from gisdrf.mixins import MercureMixin
from django.contrib.auth import get_user_model

# User Model
User = get_user_model()

class StatusList(MercureMixin, generic.ListView):
    template_name = "restaurants/sse.html"
    queryset = User.objects.all()

    mercure_subscribe_targets = ["test"]
    # mercure_publish_targets = ['status1']
    mercure_hub_topics = ["test"]
  
class StatusDetail(MercureMixin, generic.DetailView):
    template_name = "restaurants/sse.html"
    model = User


class HomeView(MercureMixin, View):
    template_name = "restaurants/index.html"

    def get(self, request, x=None, y=None, *args, **kwargs):
        """
        GET
        """
        show_hello_world.delay()
        
        context = {}

        if x and y:
            """
            Obtenemos los restaurantes más cercanos al usuario,
            a partir de las cordenadas obtenidas...
            """
            nearby_restaurants = Restaurant.objects.get_restaurants_near_pnt(x, y, results=20)
            context['restaurants'] = nearby_restaurants
            context['latitude'] = y
            context['longitude'] = x
        
        return render(request, self.template_name, context)


def get_csv_file(request, x, y):
    """
    Generamos el archivo CSV con los restaurantes ordenados
    según su distancia al usuario, y devolvemos el archivo CSV
    para su descarga...
    """

    export = generate_csv(x, y)

    # Creamos una string para nombrar al archivo a descargar.
    today = timezone.now()
    strToday = today.strftime("%Y/%m/%d-%H:%M:%S")
    file_name = "results-"+ strToday + ".csv"

    # Generamos el archivo CSV en memoria
    sheet = excel.pe.Sheet(export)

    return excel.make_response(sheet, "csv", file_name=file_name)



###
"""
LO SIGUIENTE TRATA DE UNA PRUEBA, NO FORMA PARTE
DE LA APLICACIÓN EN SI MISMA...
"""
import datetime
import time
from django.http import StreamingHttpResponse
def stream(request):
    """
    Implementación de SSE nativa con django.

    Leer más aqui:
    https://docs.djangoproject.com/en/3.0/ref/request-response/#django.http.StreamingHttpResponse
    """
    def event_stream():
        """
        Esto es un simple test para conocer el funcionamiento de 
        StreamingHttpResponse, básicamente, estará devolviendo al
        usuario una actualización de la hora correspondiente.

        Es necesario que el cliente se suscriba a este evento desde el template.

        EJ:

        <body>
            <h4>Getting server updates</h4>
            <div id="result"></div>
        </body>

        <script>
            if(typeof(EventSource) !== "undefined") {
            var source = new EventSource("{% url 'restaurants:stream' %}");
            source.onmessage = function(event) {
                console.log(event);
                document.getElementById("result").innerHTML += event.data + "<br>";
            };
            } else {
            document.getElementById("result").innerHTML = "Sorry, your browser does not support server-sent events...";
            }
        </script>
        """
        while True:
            time.sleep(3)
            yield 'data: The server time is: %s\n\n' % datetime.datetime.now()

    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')