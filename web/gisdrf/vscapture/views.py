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
        time_start = results.last().timestamp - timedelta(minutes=int(time_period))
        time_end = results.last().timestamp
        results = results.filter(timestamp__lte=time_end, timestamp__gte=time_start)

    dataset_defaults = {
        "fill": False,
        "radius": 5,
        "pointBorderWidth": 2,
        "hoverRadius": 9,
    }

    dates = results.values_list('timestamp', flat=True)
    jsonData = {
        "datasets": [],
    }

    jsonData["datasets"].append(dataset_defaults.copy())
    field_name = 'nibpSystolic'
    jsonData["datasets"][-1].update({
        "data": [{'x': row['timestamp'], 'y': row[field_name]} for row in results.values('timestamp', field_name)],
        "label": "Systolic NIBP",
        "borderColor": "#eb7d34",
        "pointStyle": 'triangle',
        "pointRotation": 180,
        "pointBackgroundColor": "#eb7d34",
    })

    jsonData["datasets"].append(dataset_defaults.copy())
    field_name = 'nibpDisatolic'
    jsonData["datasets"][-1].update({
        "data": [{'x': row['timestamp'], 'y': row[field_name]} for row in results.values('timestamp', field_name)],
        "label": "Diastolic NIBP",
        "borderColor": "#eb7d34",
        "pointStyle": 'triangle',
        "pointBackgroundColor": "#eb7d34",
    })

    jsonData["datasets"].append(dataset_defaults.copy())
    field_name = 'nibpMean'
    jsonData["datasets"][-1].update({
        "data": [{'x': row['timestamp'], 'y': row[field_name]} for row in results.values('timestamp', field_name)],
        "label": "Mean NIBP",
        "borderColor": "#8e5ea2",
        "pointStyle": 'crossRot',
    })

    jsonData["datasets"].append(dataset_defaults.copy())
    field_name = 'p1Systolic'
    jsonData["datasets"][-1].update({
        "data": [{'x': row['timestamp'], 'y': row[field_name]} for row in results.values('timestamp', field_name)],
        "label": "IBP Systolic",
        "borderColor": "#3e95cd",
        "pointStyle": 'triangle',
        "pointRotation": 180,
    })

    jsonData["datasets"].append(dataset_defaults.copy())
    field_name = 'p1Disatolic'
    jsonData["datasets"][-1].update({
        "data": [{'x': row['timestamp'], 'y': row[field_name]} for row in results.values('timestamp', field_name)],
        "label": "IBP Diastolic",
        "borderColor": "#3e95cd",
        "pointStyle": 'triangle',
    })

    jsonData["datasets"].append(dataset_defaults.copy())
    field_name = 'p1Mean'
    jsonData["datasets"][-1].update({
        "data": [{'x': row['timestamp'], 'y': row[field_name]} for row in results.values('timestamp', field_name)],
        "label": "IBP Mean",
        "borderColor": "#8e5ea2",
        "pointStyle": 'cross',
    })

    jsonData["datasets"].append(dataset_defaults.copy())
    field_name = 'ecgHr'
    jsonData["datasets"][-1].update({
        "data": [{'x': row['timestamp'], 'y': row[field_name]} for row in results.values('timestamp', field_name)],
        "label": "HR",
        "borderColor": "#c45850",
        "radius": 3,
        "pointStyle": 'circle',
        "hoverRadius": 5,
        "pointBackgroundColor": "#c45850",
    })

    jsonData["datasets"].append(dataset_defaults.copy())
    field_name = 'p1Hr'
    jsonData["datasets"][-1].update({
        "data": [{'x': row['timestamp'], 'y': row[field_name]} for row in results.values('timestamp', field_name)],
        "label": "P1 HR",
        "borderColor": "#c45850",
        "radius": 3,
        "pointStyle": 'circle',
        "hoverRadius": 5,
    })

    jsonData["datasets"].append(dataset_defaults.copy())
    field_name = 'spo2'
    jsonData["datasets"][-1].update({
        "data": [{'x': row['timestamp'], 'y': row[field_name]} for row in results.values('timestamp', field_name)],
        "label": "SPO2",
        "borderColor": "#3cba9f",
        "pointStyle": 'star',
        "borderDash": [5, 5],
    })

    jsonData["datasets"].append(dataset_defaults.copy())
    field_name = 'rr'
    jsonData["datasets"][-1].update({
        "data": [{'x': row['timestamp'], 'y': row[field_name]} for row in results.values('timestamp', field_name)],
        "label": "Respiratory Rate",
        "borderColor": "#e8ad0c",
        "radius": 3,
        "pointStyle": 'circle',
        "hoverRadius": 5,
    })

    jsonData["datasets"].append(dataset_defaults.copy())
    field_name = 't1Temp'
    jsonData["datasets"][-1].update({
        "data": [{'x': row['timestamp'], 'y': row[field_name]} for row in results.values('timestamp', field_name)],
        "label": "T1 Temperature",
        "borderColor": "#ae4ae8",
        "radius": 3,
        "pointStyle": 'rectRot',
        "hoverRadius": 5,
    })

    return JsonResponse(jsonData)
