# Generated by Django 4.2.4 on 2023-09-30 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datascraper', '0007_alter_forecast_prediction_range'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forecast',
            name='prediction_range',
        ),
        migrations.AddField(
            model_name='forecast',
            name='prediction_range_hours',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
