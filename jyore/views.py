from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Users,Profile
from .forms import SignupForm,LoginForm
from django.urls import reverse

# Create your views here.
def index(request): 
    return render(request,'jyore/index.html')


def profile_view(request):
    username = request.user
    history = Profile.objects.filter(user = username)  # Replace with your actual history data
    context = {'history': history, 'username': username}
    return render(request, 'jyore/profile.html', context)

def delete_v(request,id):
    print(id)
    user = Profile.objects.get(pk=id)
    user.delete()
    return redirect('profile')

from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.utils.crypto import get_random_string



def register(request):
    form = SignupForm()
    
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
                user.is_active = False  # Set user as inactive until OTP verification
                user.save()
                otp = get_random_string(length=6, allowed_chars='0123456789')

                # Save OTP in user profile or associated OTP model
                Users.otp = otp
                Users.save()
                form.save()
                # Send OTP via email
                subject = 'OTP Verification'
                message = f'Your OTP for registration: {otp}'
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [username]
                send_mail(subject, message, from_email, recipient_list)

                # Redirect to OTP verification page
                return redirect('verify_otp')
        else:
            return HttpResponse("Error")
    return render(request, 'jyore/register.html', {'form': form})

def verify_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        user = request.user

        # Compare the entered OTP with the saved OTP
        if otp == User.otp:
            # Mark user as verified and activate the account
            user.is_active = True
            user.save()

            messages.success(request, 'OTP verification successful. Your account is now active.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid OTP. Please enter the correct OTP.')

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

def marketplace(request): 
    cities = Profile.objects.values_list('city', flat=True).distinct()
    profiles = Profile.objects.all()
    
    # Apply filters if provided in the request
    city_filter = request.GET.get('city')
    type_filter = request.GET.get('type')
    dimensions_filter = request.GET.get('totalArea')
    price_from = request.GET.get('price_from')
    price_to = request.GET.get('price_to')
    willing_to = request.GET.get('willing_to')
    
    if city_filter:
        profiles = profiles.filter(city=city_filter)
    if type_filter:
        profiles = profiles.filter(type_of_property=type_filter)
    if dimensions_filter:
        profiles = profiles.filter(dimensions__lte=dimensions_filter)
    if price_from:
        profiles = profiles.filter(price__gte=price_from)

    if price_to:
        profiles = profiles.filter(price__lte=price_to)
    
    if willing_to:
        profiles = profiles.filter(Willing_to=willing_to)
    
    context = {
        'cities': cities,
        'profile': profiles,
    }
    
    return render(request, 'jyore/MarketPlace.html', context)



def sell(request):
    if request.method == 'POST':
        user = request.user
        Landlord_Name = request.user.first_name
        email = request.user.email
        mobile = request.POST['mobile']
        price = request.POST['price']
        length = request.POST['length']
        width = request.POST['width']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        totalArea = request.POST['totalArea']
        description = request.POST['description']
        type_of_property = request.POST['type_of_property']
        Willing_to = request.POST['Willing_to']
        facing = request.POST['facing']
        mainimage = request.FILES.get('mainimage')
        subimage1 = request.FILES.get('subimage1')
        subimage2 = request.FILES.get('subimage2')
        subimage3 = request.FILES.get('subimage3')
        
        try:
            profile = Profile(
                user=user,
                Landlord_Name=Landlord_Name,
                email=email,
                mobile=mobile,
                price=price,
                length=length,
                width=width,
                address=address,
                city=city,
                state=state,
                totalArea=totalArea,
                description=description,
                type_of_property=type_of_property,
                Willing_to=Willing_to,
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

