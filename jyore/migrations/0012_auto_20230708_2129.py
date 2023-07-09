# Generated by Django 3.2.4 on 2023-07-08 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jyore', '0011_profile_otp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='otp',
        ),
        migrations.AddField(
            model_name='users',
            name='otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
