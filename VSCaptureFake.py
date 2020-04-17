# Either run from VSCaptureWeb by changing the executable name
# or run manually like so:
# python VSCaptureFake.py -port /dev/cu.Bluetooth-Incoming-Port -interval 15 -waveset 1 -export 2 -devid foobar -url http://localhost:8000/

import json
import sys
import time
from datetime import datetime

import requests


def get_data(**k):

    timestamp = f"{k['day']}~{k['month']}~{k['year']} {k['hour']}:{k['minute']}:{k['second']}"
    return [
      {
        "DeviceID": k['devid'],
        "PhysioID": "ECG_HR",
        "Timestamp": timestamp,
        "Value": "0"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "NIBP_Systolic",
        "Timestamp": timestamp,
        "Value": "-"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "NIBP_Diastolic",
        "Timestamp": timestamp,
        "Value": "-"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "NIBP_Mean",
        "Timestamp": timestamp,
        "Value": "-"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "SpO2",
        "Timestamp": timestamp,
        "Value": "97"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "ET_CO2",
        "Timestamp": timestamp,
        "Value": "0"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "AA_ET",
        "Timestamp": timestamp,
        "Value": "0"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "AA_FI",
        "Timestamp": timestamp,
        "Value": "0"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "AA_MAC_SUM",
        "Timestamp": timestamp,
        "Value": "0"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "Agent_AA",
        "Timestamp": timestamp,
        "Value": "ISO"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "O2_FI",
        "Timestamp": timestamp,
        "Value": "98.5"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "N2O_FI",
        "Timestamp": timestamp,
        "Value": "0"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "N2O_ET",
        "Timestamp": timestamp,
        "Value": "0"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "CO2_RR",
        "Timestamp": timestamp,
        "Value": "0"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "T1_Temp",
        "Timestamp": timestamp,
        "Value": "35.55"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "T2_Temp",
        "Timestamp": timestamp,
        "Value": "-"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "P1_HR",
        "Timestamp": timestamp,
        "Value": "0"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "P1_Systolic",
        "Timestamp": timestamp,
        "Value": "76"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "P1_Disatolic",
        "Timestamp": timestamp,
        "Value": "76"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "P1_Mean",
        "Timestamp": timestamp,
        "Value": "76"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "P2_HR",
        "Timestamp": timestamp,
        "Value": "0"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "P2_Systolic",
        "Timestamp": timestamp,
        "Value": "0"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "P2_Diastolic",
        "Timestamp": timestamp,
        "Value": "-2"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "P2_Mean",
        "Timestamp": timestamp,
        "Value": "-1"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "PPeak",
        "Timestamp": timestamp,
        "Value": "-"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "PPlat",
        "Timestamp": timestamp,
        "Value": "-"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "TV_Exp",
        "Timestamp": timestamp,
        "Value": "-"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "TV_Insp",
        "Timestamp": timestamp,
        "Value": "-"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "PEEP",
        "Timestamp": timestamp,
        "Value": "-"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "MV_Exp",
        "Timestamp": timestamp,
        "Value": "-"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "Compliance",
        "Timestamp": timestamp,
        "Value": "-"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "RR",
        "Timestamp": timestamp,
        "Value": "-"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "ST_II",
        "Timestamp": timestamp,
        "Value": "-"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "ST_V5",
        "Timestamp": timestamp,
        "Value": "-"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "ST_aVL",
        "Timestamp": timestamp,
        "Value": "-"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "EEG_Entropy",
        "Timestamp": timestamp,
        "Value": "0"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "EMG_Entropy",
        "Timestamp": timestamp,
        "Value": "0"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "BSR_Entropy",
        "Timestamp": timestamp,
        "Value": "0"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "BIS",
        "Timestamp": timestamp,
        "Value": "0"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "BIS_BSR",
        "Timestamp": timestamp,
        "Value": "0"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "BIS_EMG",
        "Timestamp": timestamp,
        "Value": "0"
      },
      {
        "DeviceID": k['devid'],
        "PhysioID": "BIS_SQI",
        "Timestamp": timestamp,
        "Value": "0"
      }
    ]


if __name__ == "__main__":

    # Grab pairs of args as a dict (quick and dirty argparse)
    pairs = zip(sys.argv[1::2], sys.argv[2::2])
    args = dict((x[0][1:], x[1]) for x in pairs)

    while True:
        timestamp = datetime.now()
        data = json.dumps(get_data(
            **{'devid': args['devid'],
               'year': timestamp.year,
               'month': timestamp.month,
               'day': timestamp.day,
               'hour': timestamp.hour,
               'minute': timestamp.minute,
               'second': timestamp.second,
        }))
        data = data.replace("~", "\/")
        x = requests.post(args['url'], data=data)
        time.sleep(int(args['interval']))