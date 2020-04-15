from django.contrib.gis.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


def Range(min=0, max=100):
    return [MinValueValidator(min), MaxValueValidator(max)]


class LogRow(models.Model):

    agentAAChoices = ["ISO", "SEV", "DES"]

    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_created=True, null=True, blank=True)
    ecgHr = models.IntegerField("ECG HR", validators=Range(0,100), null=True, blank=True)
    nibpSystolic = models.IntegerField("NIBP Systolic", validators=Range(0,100), null=True, blank=True)
    nibpDiastolic = models.IntegerField("NIBP Diastolic", validators=Range(0,100), null=True, blank=True)
    nibpMean = models.IntegerField("NIBP Mean", validators=Range(0,100), null=True, blank=True)
    spo2 = models.IntegerField("SpO2", validators=Range(0,100), null=True, blank=True)
    etCo2 = models.IntegerField("ET CO2", validators=Range(0,100), null=True, blank=True)
    aaEt = models.FloatField("AA ET", validators=Range(0,100), null=True, blank=True)
    aaFi = models.FloatField("AA FI", validators=Range(0,100), null=True, blank=True)
    aaMacSum = models.FloatField("AA MAC SUM", validators=Range(0,100), null=True, blank=True)
    agentAa = models.TextField("Agent AA", choices=zip(agentAAChoices, agentAAChoices), null=True, blank=True)
    o2Fi = models.FloatField("O2 FI", validators=Range(0,100), null=True, blank=True)
    n2OFi = models.FloatField("N2O FI", validators=Range(0,100), null=True, blank=True)
    n2OEt = models.FloatField("N2O ET", validators=Range(0,100), null=True, blank=True)
    co2Rr = models.IntegerField("CO2 RR", validators=Range(0,100), null=True, blank=True)
    t1Temp = models.FloatField("T1 TEMP", validators=Range(0,100), null=True, blank=True)
    t2Temp = models.FloatField("T2 TEMP", validators=Range(0,100), null=True, blank=True)
    p1Hr = models.IntegerField("P1 HR", validators=Range(0,100), null=True, blank=True)
    p1Systolic = models.IntegerField("P1 Systolic", validators=Range(0,100), null=True, blank=True)
    p1Disatolic = models.IntegerField("P1 Disatolic", validators=Range(0,100), null=True, blank=True)
    p1Mean = models.IntegerField("P1 Mean", validators=Range(0,100), null=True, blank=True)
    p2Hr = models.IntegerField("P2 HR", validators=Range(0,100), null=True, blank=True)
    p2Systolic = models.IntegerField("P2 Systolic", validators=Range(0,100), null=True, blank=True)
    p2Diastolic = models.IntegerField("P2 Diastolic", validators=Range(0,100), null=True, blank=True)
    p2Mean = models.IntegerField("P2 Mean", validators=Range(0,100), null=True, blank=True)
    ppeak = models.IntegerField("PPeak", validators=Range(0,100), null=True, blank=True)
    pplat = models.IntegerField("PPlat", validators=Range(0,100), null=True, blank=True)
    tvExp = models.IntegerField("TV Exp", validators=Range(0,100), null=True, blank=True)
    tvInsp = models.IntegerField("TV Insp", validators=Range(0,100), null=True, blank=True)
    peep = models.IntegerField("PEEP", validators=Range(0,100), null=True, blank=True)
    mvExp = models.IntegerField("MV Exp", validators=Range(0,100), null=True, blank=True)
    compliance = models.FloatField("Compliance", validators=Range(0,100), null=True, blank=True)
    rr = models.IntegerField("RR", validators=Range(0,100), null=True, blank=True)
    stIi = models.FloatField("ST II", validators=Range(0,100), null=True, blank=True)
    stV5 = models.FloatField("ST V5", validators=Range(0,100), null=True, blank=True)
    stAvl = models.FloatField("ST aVL", validators=Range(0,100), null=True, blank=True)
    eegEntropy = models.IntegerField("EEG Entropy", validators=Range(0,100), null=True, blank=True)
    emgEntropy = models.IntegerField("EMG Entropy", validators=Range(0,100), null=True, blank=True)
    bsrEntropy = models.IntegerField("BSR Entropy", validators=Range(0,100), null=True, blank=True)
    bis = models.IntegerField("BIS", validators=Range(0,100), null=True, blank=True)
    bisBsr = models.IntegerField("BIS BSR", validators=Range(0,100), null=True, blank=True)
    bisEmg = models.IntegerField("BIS EMG", validators=Range(0,100), null=True, blank=True)
    bisSqi = models.IntegerField("BIS SQI", validators=Range(0,100), null=True, blank=True)
