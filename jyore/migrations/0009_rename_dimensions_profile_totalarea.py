# Generated by Django 3.2.4 on 2023-07-08 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jyore', '0008_profile_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='dimensions',
            new_name='totalArea',
        ),
    ]
