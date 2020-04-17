# Generated by Django 3.0.5 on 2020-04-14 15:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vscapture', '0002_logrow_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='logrow',
            name='aaEt',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='AA ET'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='aaFi',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='AA FI'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='aaMacSum',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='AA MAC SUM'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='agentAa',
            field=models.TextField(choices=[('ISO', 'ISO'), ('SEV', 'SEV'), ('DES', 'DES')], default=0, verbose_name='Agent AA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='bis',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='BIS'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='bisBsr',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='BIS BSR'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='bisEmg',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='BIS EMG'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='bisSqi',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='BIS SQI'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='bsrEntropy',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='BSR Entropy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='co2Rr',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='CO2 RR'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='compliance',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Compliance'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='ecgHr',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='ECG HR'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='eegEntropy',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='EEG Entropy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='emgEntropy',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='EMG Entropy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='etCo2',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='ET CO2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='mvExp',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='MV Exp'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='n2OEt',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='N2O ET'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='n2OFi',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='N2O FI'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='nibpDiastolic',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='NIBP Diastolic'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='nibpMean',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='NIBP Mean'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='nibpSystolic',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='NIBP Systolic'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='o2Fi',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='O2 FI'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='p1Disatolic',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='P1 Disatolic'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='p1Hr',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='P1 HR'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='p1Mean',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='P1 Mean'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='p1Systolic',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='P1 Systolic'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='p2Diastolic',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='P2 Diastolic'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='p2Hr',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='P2 HR'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='p2Mean',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='P2 Mean'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='p2Systolic',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='P2 Systolic'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='peep',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='PEEP'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='ppeak',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='PPeak'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='pplat',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='PPlat'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='rr',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='RR'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='spo2',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='SpO2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='stAvl',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='ST aVL'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='stIi',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='ST II'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='stV5',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='ST V5'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='t1Temp',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='T1 TEMP'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='t2Temp',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='T2 TEMP'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='tvExp',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='TV Exp'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logrow',
            name='tvInsp',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='TV Insp'),
            preserve_default=False,
        ),
    ]