from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.
class Users(models.Model):
    
    
    First_Name = models.CharField(max_length=100)
    Email = models.EmailField( max_length=254)
    password = models.CharField(max_length=20,default='pass')
    def __str__(self):
        return self.First_Name

User = get_user_model()
class Profile(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)  # New field for user
    Landlord_Name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30, default="Andhra Pradesh") 
    mainimage = models.ImageField(upload_to="account/images", default="none")
    subimage1 = models.ImageField(upload_to="account/images", default="none")
    subimage2 = models.ImageField(upload_to="account/images", default="none")
    subimage3 = models.ImageField(upload_to="account/images", default="none")
    dimensions = models.CharField(max_length=50, default="0")
    CHOICES = (
        ('land', 'Land'),
        ('house', 'House'),
        ('commercial space', 'Commercial Space'),
    )
    type_of_property = models.CharField(max_length=20, choices=CHOICES, default="house")

    def __str__(self):
        return self.Landlord_Name 