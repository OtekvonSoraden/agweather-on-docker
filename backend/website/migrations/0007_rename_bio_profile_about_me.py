# Generated by Django 4.2.4 on 2023-11-07 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_remove_profile_location_profile_favorite_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='bio',
            new_name='about_me',
        ),
    ]
