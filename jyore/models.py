from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.
class Users(models.Model):
    
    
    First_Name = models.CharField(max_length=100)
    Email = models.EmailField( max_length=254)
    password = models.CharField(max_length=20,default='pass')
    otp = models.CharField(max_length=6, blank=True, null=True)  # OTP field
    def __str__(self):
        return self.First_Name

User = get_user_model()
class Profile(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    Landlord_Name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True, default=0)
    length = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30, default="Andhra Pradesh") 
    totalArea = models.CharField(max_length=50, default="0")
    description = models.TextField(max_length=500, default="none")
    CHOICES = (
        ('land', 'Land'),
        ('house', 'House'),
        ('commercial space', 'Commercial Space'),
    )
    type_of_property = models.CharField(max_length=20, choices=CHOICES, default="house")

    Willing_to_CHOICES = (
        ('sell', 'Sell'),
        ('rent', 'Rent'),
    )
    Willing_to = models.CharField(max_length=20, choices=Willing_to_CHOICES, default="sell")
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
    facing = models.CharField(max_length=20, choices=facing_choices, default="east")
    mainimage = models.ImageField(upload_to="account/images", default="none")
    subimage1 = models.ImageField(upload_to="account/images", default="none")
    subimage2 = models.ImageField(upload_to="account/images", default="none")
    subimage3 = models.ImageField(upload_to="account/images", default="none")
    
    
    def __str__(self):
        return self.Landlord_Name