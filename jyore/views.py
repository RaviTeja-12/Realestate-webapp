from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Users,Profile,Otp
from .forms import SignupForm,LoginForm
from django.urls import reverse

# Create your views here.
def index(request): 
    return render(request,'jyore/index.html')


def profile_view(request):
    username = request.user
    houseprofile = Profile.objects.filter(user = username)  # Replace with your actual history data
    landprofile = landProfile.objects.filter(user = username)
    history = list(chain(houseprofile, landprofile))
    context = {'history': history, 'username': username}
    return render(request, 'jyore/profile.html', context)

from django.shortcuts import get_object_or_404, redirect
from .models import Profile, landProfile

def delete_v(request, id):
    # Try to get the profile from the Profile model based on the provided 'id'
    
    user = Profile.objects.get(pk=id)
    user.delete()
    return redirect('profile')

def delete_land(request, id):
    # Try to get the profile from the Profile model based on the provided 'id'

    user = landProfile.objects.get(pk=id)
    user.delete()
    return redirect('profile')

    

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.utils.crypto import get_random_string



def register(request):
    form = SignupForm()
     # Create an empty list to store users
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = request.POST["Email"]
            password = request.POST["password"]
            first_name = request.POST["First_Name"]
            if Users.objects.filter(Email=username).exists():
                messages.info(request, 'Email already exists!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name)
                user.save()
                form.save()
                
                 # Append the user to the list
                # Assuming you have the otp and user objects available
                otp = generate_otp()
                otp_instance = Otp.objects.create(otp=otp, email=username)
                send_otp(username, otp_instance.otp)
                return redirect('verify_otp', username=username)
        else:
            return HttpResponse("not valid")
    
    context = {'form': form}  # Pass the user_list to the context
    return render(request, 'jyore/register.html', context)

def verify_otp(request, username):
    if request.method == 'POST':
        otp = request.POST['otp']
        if Otp.objects.filter(otp=otp).exists() and Otp.objects.filter(email=username).exists():
            return redirect('home')
        else:
            messages.info(request, 'Invalid OTP!')
            return redirect('verify_otp')
    
    # Send OTP via email
    return render(request, 'jyore/otp-verification.html')

def login_page(request):
    form=LoginForm()
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Email']
            password = form.cleaned_data['password']
            user=auth.authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                request.session['authenticated'] = True
                return redirect('home')
            else:
                messages.info(request,'Invalid Email or Password!')
                return redirect('login')
        else:
            messages.info(request,'form is not valid')
            return redirect('login')
    else:
        context ={'form': form}
        return render(request,'jyore/login.html',context)


def logout_view(request):
    logout(request)
    return redirect('login')

from itertools import chain
@login_required(login_url='login')
def marketplace(request): 
    profile_cities = Profile.objects.values_list('city', flat=True).distinct()

# Retrieve cities from LandProfile model
    landprofile_cities = landProfile.objects.values_list('city', flat=True).distinct()

# Combine the two lists using chain()
    cities = list(chain(profile_cities, landprofile_cities))
    houseprofiles = Profile.objects.all()
    landprofiles = landProfile.objects.all()
    
    # Apply filters if provided in the request
    city_filter = request.GET.get('city')
    type_filter = request.GET.get('type')
    dimensions_filter = request.GET.get('totalArea')
    price_from = request.GET.get('price_from')
    price_to = request.GET.get('price_to')
    willing_to = request.GET.get('willing_to')
    
    if type_filter == 'land':
        houseprofiles=None
        if city_filter:
            landprofiles = landprofiles.filter(city=city_filter)
        if type_filter:
            landprofiles = landprofiles.filter(type=type_filter)
        if dimensions_filter:
            landprofiles = landprofiles.filter(dimensions__lte=dimensions_filter)
        if price_from:
            landprofiles = landprofiles.filter(price__gte=price_from)
        if price_to:
            landprofiles = landprofiles.filter(price__lte=price_to)
        if willing_to:
            landprofiles = landprofiles.filter(Willing_to=willing_to)
    elif type_filter == 'house':
        landprofiles=None
        if city_filter:
            houseprofiles = houseprofiles.filter(city=city_filter)
        if type_filter:
            houseprofiles = houseprofiles.filter(type=type_filter)
        if dimensions_filter:
            houseprofiles = houseprofiles.filter(dimensions__lte=dimensions_filter)
        if price_from:
            houseprofiles = houseprofiles.filter(price__gte=price_from)
        if price_to:
            houseprofiles = houseprofiles.filter(price__lte=price_to)
        if willing_to:
            houseprofiles = houseprofiles.filter(Willing_to=willing_to) 
    context = {
        'cities': cities,
        'profile': houseprofiles,
        'landprofile': landprofiles,
    }
    
    return render(request, 'jyore/MarketPlace.html', context)



# views.py


from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Profile

def housesellerprofile(request):
    if request.method == 'POST':
        user = request.user
        Landlord_Name = request.user.first_name
        email = request.user.username
        mobile = request.POST.get('mobile')
        sellprice = request.POST.get('sellprice')
        rentprice = request.POST.get('rentprice')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        totalArea = request.POST.get('totalArea')
        description = request.POST.get('description')
        bedrooms = request.POST.get('bedrooms')
        bathrooms = request.POST.get('bathrooms')
        dimensions_of_bedroom = request.POST.get('dimensions_of_bedroom')
        facing_road_width = request.POST.get('facing_road_width')
        wardrobe = request.POST.get('wardrobe')
        fans = request.POST.get('fans')
        lights = request.POST.get('lights')
        kitchen = request.POST.get('kitchen')
        ac = request.POST.get('ac')
        beds = request.POST.get('beds')
        chimney = request.POST.get('chimney')
        private_garden = request.POST.get('private_garden')
        maintenance_staff = request.POST.get('maintenance_staff')
        security = request.POST.get('security')
        drinage = request.POST.get('drinage')
        swimming_pool = request.POST.get('swimming_pool')
        gym = request.POST.get('gym')
        lift = request.POST.get('lift')
        internet = request.POST.get('internet')
        water_source = request.POST.get('water_source')
        gated_community = request.POST.get('gated_community')
        parking = request.POST.get('parking')
        flooring = request.POST.get('flooring')
        age_of_property = request.POST.get('age_of_property')
        furnished = request.POST.get('furnished')
        Willing_to = request.POST.get('Willing_to')
        status = request.POST.get('status')
        facing = request.POST.get('facing')
        mainimage = request.FILES.get('mainimage')
        subimage1 = request.FILES.get('subimage1')
        subimage2 = request.FILES.get('subimage2')
        subimage3 = request.FILES.get('subimage3')
        if Willing_to == 'sell':
            rentprice = 0
        elif Willing_to == 'rent':
            sellprice = 0
        # Perform any necessary form validation here before creating the profile
        # For example, check if required fields are not empty, validate numeric values, etc.
        try:
            profile = Profile(
                user=user,
                Landlord_Name=Landlord_Name,
                email=email,
                mobile=mobile,
                sellprice=sellprice,
                rentprice=rentprice,
                address=address,
                city=city,
                state=state,
                totalArea=totalArea,
                description=description,
                bedrooms=bedrooms,
                bathrooms=bathrooms,
                dimensions_of_bedroom=dimensions_of_bedroom,
                facing_road_width=facing_road_width,
                wardrobe=wardrobe,
                fans=fans,
                lights=lights,
                kitchen=kitchen,
                ac=ac,
                beds=beds,
                chimney=chimney,
                private_garden=private_garden,
                maintenance_staff=maintenance_staff,
                security=security,
                drinage=drinage,
                swimming_pool=swimming_pool,
                gym=gym,
                lift=lift,
                internet=internet,
                water_source=water_source,
                gated_community=gated_community,
                parking=parking,
                flooring=flooring,
                age_of_property=age_of_property,
                furnished=furnished,
                Willing_to=Willing_to,
                status=status,
                facing=facing,
                mainimage=mainimage,
                subimage1=subimage1,
                subimage2=subimage2,
                subimage3=subimage3
            )
            profile.save()
            messages.success(request, 'Profile created successfully.')
            return redirect('marketplace')
        except Exception as e:
            return HttpResponse(e)
            
    return render(request, 'jyore/sell.html')




import string
import random
from django.conf import settings
from django.core.mail import send_mail

def generate_otp():
    digits = string.digits
    otp = ''.join(random.choice(digits) for _ in range(6))
    return otp


def send_otp(email, otp):
    subject = 'OTP Verification'
    message = f'Your OTP for registration: {otp}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)


def viewproperty(request, id):
    profile = Profile.objects.get(id=id)
    context = {
        'profile': profile,
    }
    return render(request, 'jyore/viewproperty.html', context)

def sellfirst(request):
    return render(request, 'jyore/sellfirst.html')


from django.shortcuts import render, redirect
from .models import landProfile

def landsellerprofile(request):
    if request.method == 'POST':
        # Get the form data from the request.POST dictionary
        user = request.user
        Landlord_Name = request.user.first_name
        email = request.user.username
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state', 'Andhra Pradesh')  # Default value if state is not provided
        country = request.POST.get('country', 'India')  # Default value if country is not provided
        pincode = request.POST.get('pincode')
        land_type = request.POST.get('land_type', 'corner')  # Default value if land_type is not provided
        length = request.POST.get('length')
        breadth = request.POST.get('breadth')
        metric = request.POST.get('metric', 'sq.ft')  # Default value if metric is not provided
        price = request.POST.get('price')
        willing_to = request.POST.get('Willing_to', 'sell')  # Default value if Willing_to is not provided
        mainimage = request.FILES.get('mainimage')
        subimage1 = request.FILES.get('subimage1')
        subimage2 = request.FILES.get('subimage2')
        subimage3 = request.FILES.get('subimage3')

        # Create a new landProfile object and save it to the database
        profile = landProfile(
            user=user,
            Landlord_Name=Landlord_Name,
            email=email,
            mobile=mobile,
            address=address,
            city=city,
            state=state,
            country=country,
            pincode=pincode,
            land_type=land_type,
            length=length,
            breadth=breadth,
            metric=metric,
            price=price,
            Willing_to=willing_to,
            mainimage=mainimage,
            subimage1=subimage1,
            subimage2=subimage2,
            subimage3=subimage3
        )
        
        # Assuming you are using User authentication, set the user for the profile
        profile.user = request.user
        profile.save()
        messages.success(request, 'Profile created successfully.')
        return redirect('marketplace')
        # Redirect to the detail page of the newly created profile
    return render(request, 'jyore/landsell.html')


def landviewproperty(request, id):
    profile = landProfile.objects.get(id=id)
    context = {
        'profile': profile,
    }
    return render(request, 'jyore/landviewproperty.html', context)