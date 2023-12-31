# Generated by Django 4.2.2 on 2023-06-22 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jyore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Landlord_Name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('state', models.CharField(default='Andhra Pradesh', max_length=30)),
                ('mainimage', models.ImageField(default='', upload_to='account/images')),
                ('subimage1', models.ImageField(default='', upload_to='account/images')),
                ('subimage2', models.ImageField(default='', upload_to='account/images')),
                ('subimage3', models.ImageField(default='', upload_to='account/images')),
            ],
        ),
    ]
