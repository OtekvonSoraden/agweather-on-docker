# Generated by Django 4.2.4 on 2023-09-30 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datascraper', '0005_alter_forecast_prediction_range'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forecast',
            name='prediction_range',
            field=models.DateTimeField(default=None),
        ),
    ]
