from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.


class Users(models.Model):

    First_Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=254)
    password = models.CharField(max_length=20, default='pass')

    def __str__(self):
        return self.First_Name


class Otp(models.Model):
    otp = models.CharField(max_length=6)
    email = models.EmailField(
        max_length=254, default='email', null=True, blank=True)

    def __str__(self):
        return self.otp

    def save_otp(self, otp):
        self.otp = otp
        self.save()


User = get_user_model()
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    Landlord_Name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.IntegerField(blank=True, null=True)
    sellprice = models.IntegerField(blank=True, null=True, default=0)
    rentprice = models.IntegerField(blank=True, null=True, default=0)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30, default="Andhra Pradesh")
    totalArea = models.CharField(max_length=50, default="0")
    description = models.TextField(max_length=500, default="none")
    bedrooms = models.IntegerField(blank=True, null=True, default=0)
    bathrooms = models.IntegerField(blank=True, null=True, default=0)
    dimensions_of_bedroom = models.CharField(max_length=50, default="0")
    facing_road_width = models.IntegerField(blank=True, null=True, default=0)
    wardrobe_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    wardrobe = models.CharField(
        max_length=20, choices=wardrobe_choices, default="no")
    fans = models.IntegerField(blank=True, null=True, default=0)
    lights = models.IntegerField(blank=True, null=True, default=0)
    kitchen_choices = (
        ('modular', 'Modular'),
        ('normal', 'Normal'),
    )
    kitchen = models.CharField(
        max_length=20, choices=kitchen_choices, default="normal")
    ac_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    ac = models.CharField(max_length=20, choices=ac_choices, default="no")
    beds = models.IntegerField(blank=True, null=True, default=0)
    chimney_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    chimney = models.CharField(
        max_length=20, choices=chimney_choices, default="no")
    dining_table_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    dining_table = models.CharField(
        max_length=20, choices=dining_table_choices, default="no")
    exhaust_fan_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    exhaust_fan = models.CharField(
        max_length=20, choices=exhaust_fan_choices, default="no")
    fridge_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    fridge = models.CharField(
        max_length=20, choices=fridge_choices, default="no")
    geysers_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    geysers = models.CharField(
        max_length=20, choices=geysers_choices, default="no")
    microwave_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    microwave = models.CharField(
        max_length=20, choices=microwave_choices, default="no")
    sofa_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    sofa = models.CharField(max_length=20, choices=sofa_choices, default="no")
    washing_machine_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    washing_machine = models.CharField(
        max_length=20, choices=washing_machine_choices, default="no")
    tv_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    tv = models.CharField(max_length=20, choices=tv_choices, default="no")
    water_purifier_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    water_purifier = models.CharField(
        max_length=20, choices=water_purifier_choices, default="no")
    vasthu_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    vasthu = models.CharField(
        max_length=20, choices=vasthu_choices, default="no")
    private_garden_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    private_garden = models.CharField(
        max_length=20, choices=private_garden_choices, default="no")
    maintenance_staff_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    maintenance_staff = models.CharField(
        max_length=20, choices=maintenance_staff_choices, default="no")
    security_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    security = models.CharField(
        max_length=20, choices=security_choices, default="no")
    drinage_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    drinage = models.CharField(
        max_length=20, choices=drinage_choices, default="no")
    swimming_pool_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    swimming_pool = models.CharField(
        max_length=20, choices=swimming_pool_choices, default="no")
    gym_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    gym = models.CharField(max_length=20, choices=gym_choices, default="no")
    lift_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    lift = models.CharField(max_length=20, choices=lift_choices, default="no")
    internet_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    water_source_choices = (
        ('borewell', 'Borewell'),
        ('municipal', 'Municipal'),
        ('both', 'Both'),
    )
    water_source = models.CharField(
        max_length=20, choices=water_source_choices, default="borewell")
    gated_community_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    gated_community = models.CharField(
        max_length=20, choices=gated_community_choices, default="no")
    parking_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    parking = models.CharField(
        max_length=20, choices=parking_choices, default="no")
    flooring_choices = (
        ('marble', 'Marble'),
        ('tiles', 'Tiles'),
        ('wooden', 'Wooden'),
        ('cement', 'Cement'),
    )
    flooring = models.CharField(
        max_length=20, choices=flooring_choices, default="marble")
    age_of_property = models.IntegerField(blank=True, null=True, default=0)
    furnished_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    furnished = models.CharField(
        max_length=20, choices=furnished_choices, default="no")
    Willing_to_CHOICES = (
        ('sell', 'Sell'),
        ('rent', 'Rent'),
    )
    Willing_to = models.CharField(
        max_length=20, choices=Willing_to_CHOICES, default="sell")
    status_CHOICES = (
        ('Ready to be occupied', 'Ready to be occupied'),
        ('In construction', 'In construction'),
    )
    status = models.CharField(
        max_length=50, choices=status_CHOICES, default="Ready to be occupied")
    facing_choices = (
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
        ('north-east', 'North-East'),
        ('north-west', 'North-West'),
        ('south-east', 'South-East'),
        ('south-west', 'South-West'),
    )
    facing = models.CharField(
        max_length=20, choices=facing_choices, default="east")
    mainimage = models.ImageField(upload_to="account/images", default="none")
    subimage1 = models.ImageField(upload_to="account/images", default="none")
    subimage2 = models.ImageField(upload_to="account/images", default="none")
    subimage3 = models.ImageField(upload_to="account/images", default="none")

    def __str__(self):
        return self.Landlord_Name