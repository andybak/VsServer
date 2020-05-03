from django.contrib import admin

from .models import LogRow


@admin.register(LogRow)
class LogRowAdmin(admin.ModelAdmin):

    list_display = [
        "name", "timestamp", "ecgHr", "nibpSystolic", "nibpDiastolic", "nibpMean", "spo2", "etCo2", "aaEt", "aaFi",
        "aaMacSum", "agentAa", "o2Fi", "n2OFi", "n2OEt", "co2Rr", "t1Temp", "t2Temp", "p1Hr", "p1Systolic",
        "p1Disatolic", "p1Mean", "p2Hr", "p2Systolic", "p2Diastolic", "p2Mean", "ppeak", "pplat", "tvExp", "tvInsp",
        "peep", "mvExp", "compliance", "rr", "stIi", "stV5", "stAvl", "eegEntropy", "emgEntropy", "bsrEntropy", "bis",
        "bisBsr", "bisEmg", "bisSqi",
    ]

    list_filter = ['name', 'timestamp']

    class Media:
        js = (
            'app/js/myscript.js',
        )
