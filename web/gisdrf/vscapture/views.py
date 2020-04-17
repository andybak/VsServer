import csv
import json

import dateutil.parser

from django.template.response import TemplateResponse
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
