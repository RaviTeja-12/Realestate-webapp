# Generated by Django 3.2.4 on 2023-07-16 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jyore', '0021_auto_20230716_1121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='age_of_property',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='ac',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bathrooms',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bedrooms',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='beds',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='chimney',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='dimensions_of_bedroom',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='dining_table',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='drinage',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='exhaust_fan',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='facing_road_width',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='fans',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='flooring',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='fridge',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='furnished',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='gated_community',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='geysers',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='gym',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='kitchen',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lift',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lights',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='maintenance_staff',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='microwave',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='parking',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='private_garden',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='rentprice',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='security',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sellprice',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sofa',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='status',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='swimming_pool',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='tv',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='vasthu',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='wardrobe',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='washing_machine',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='water_purifier',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='water_source',
        ),
        migrations.AddField(
            model_name='profile',
            name='length',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='type_of_property',
            field=models.CharField(choices=[('land', 'Land'), ('house', 'House'), ('commercial space', 'Commercial Space')], default='house', max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
