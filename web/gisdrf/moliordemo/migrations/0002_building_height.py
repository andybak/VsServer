# Generated by Django 3.0.3 on 2020-04-04 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moliordemo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='height',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]