import csv

import dateutil.parser

from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt

from .csv_mapping import csv_mapping
from .models import LogRow


@csrf_exempt
def index(request):

    if request.method == "POST":
        body = request.body.decode("utf-8").splitlines()
        capture_version = body[0]
        device_name = body[1]
        for row in csv.DictReader(body[2:], delimiter=","):
            date = None
            time = None
            row_instance = LogRow(name=device_name)
            for k, v in row.items():
                print(k, v)
                if k is None:
                    continue
                if k == "Date":
                    date = v
                elif k == "Time":
                    time = v
                    if date is not None and time is not None:
                        pass
                        row_instance.timestamp = dateutil.parser.parse(f'{date} {time}')
                else:
                    if v == "-":
                        val = None
                    elif v == "None":
                        val = None
                    else:
                        val = v
                    if val is not None:
                        setattr(row_instance, csv_mapping[k.strip()], val)
                    print(k, val, type(val))
            row_instance.save()

    context = {}

    template = "vscapture/index.html"
    return TemplateResponse(request, template, context)
