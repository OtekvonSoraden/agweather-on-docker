# Generated by Django 4.2.4 on 2023-10-04 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datascraper', '0009_forecasttemplate_last_scraped'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forecasttemplate',
            name='last_scraped',
            field=models.DateTimeField(),
        ),
    ]