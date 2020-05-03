import csv
import json
from datetime import timedelta

import dateutil.parser
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from django.template.response import TemplateResponse
from django.utils import timezone
from django.utils.dateformat import DateFormat
from django.utils.datetime_safe import datetime
from django.views.decorators.csrf import csrf_exempt

from .mapping import mapping
from .models import LogRow


@csrf_exempt
def index(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        row_instance = LogRow(name=json_data[0]['DeviceID'])
        timestamp = json_data[0]['Timestamp'].replace("\\/", "-")
        # TODO set a timezone
        row_instance.timestamp = dateutil.parser.parse(timestamp)
        
        for item in json_data:
            key = item['PhysioID']
            val = item['Value']
            if val in ["None", "-", ""]: val = None
            
            if val is not None:
                setattr(row_instance, mapping[key.strip()], val)
        row_instance.save()
    
    context = {}
    
    template = "vscapture/index.html"
    return TemplateResponse(request, template, context)


@login_required
def chart_data(request, device, time_period):
    results = LogRow.objects.all()
    
    if device != 'all':
        results = results.filter(name__iexact=device)
    
    if time_period != 'all':
        time_start = timezone.now() - timedelta(hours=int(time_period))
        time_end = timezone.now()
        results = results.filter(timestamp__lte=time_end, timestamp__gte=time_start)
    
    dataset_defaults = {
        "fill": False,
        "radius": 5,
        "pointBorderWidth": 2,
        "hoverRadius": 9,
    }

    def takespread(sequence, num):
        length = float(len(sequence))
        for i in range(num):
            yield sequence[int(ceil(i * length / num))]
    
    dates = results.values_list('timestamp', flat=True)
    jsonData = {
        "labels": [
            DateFormat(d).format('D j/m H:i:s')
            for d in dates
        ],
        "datasets": [],
    }
    
    jsonData["datasets"].append(dataset_defaults.copy())
    jsonData["datasets"][-1].update({
        "data": list(results.values_list('p1Systolic', flat=True)),
        "label": "Systolic BP",
        "borderColor": "#eb7d34",
        "pointStyle": 'triangle',
        "pointRotation": 180,
    })

    jsonData["datasets"].append(dataset_defaults.copy())
    jsonData["datasets"][-1].update({
        "data": list(results.values_list('p1Disatolic', flat=True)),
        "label": "Diastolic BP",
        "borderColor": "#3e95cd",
        "pointStyle": 'triangle',
    })

    jsonData["datasets"].append(dataset_defaults.copy())
    jsonData["datasets"][-1].update({
        "data": list(results.values_list('p1Mean', flat=True)),
        "label": "Mean BP",
        "borderColor": "#8e5ea2",
        "pointStyle": 'crossRot',
    })

    jsonData["datasets"].append(dataset_defaults.copy())
    jsonData["datasets"][-1].update({
        "data": list(results.values_list('p1Hr', flat=True)),
        "label": "HR",
        "borderColor": "#c45850",
        "radius": 3,
        "pointStyle": 'circle',
        "hoverRadius": 5,
    })

    jsonData["datasets"].append(dataset_defaults.copy())
    jsonData["datasets"][-1].update({
        "data": list(results.values_list('spo2', flat=True)),
        "label": "SPO2",
        "borderColor": "#3cba9f",
        "pointStyle": 'star',
        "borderDash": [5, 5],
    })
    
    return JsonResponse(jsonData)
