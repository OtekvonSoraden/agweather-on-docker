# Generated by Django 4.2.4 on 2023-09-30 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datascraper', '0003_rename_data_json_forecast_forecast_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='forecast',
            name='prediction_range',
            field=models.DateTimeField(default=None),
        ),
    ]
