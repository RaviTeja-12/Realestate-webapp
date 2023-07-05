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
    context = {'history': history}
    return render(request, 'jyore/profile.html', context)

def delete_v(request,id):
    print(id)
    user = Profile.objects.get(pk=id)
    user.delete()
    return redirect('profile')

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
                return redirect('login')
        else:
            return HttpResponse("not valid")
    
    context = {'form': form}  # Pass the user_list to the context
    return render(request, 'jyore/register.html', context)


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
    dimensions_filter = request.GET.get('dimensions')
    price_filter = request.GET.get('price')
    
    if city_filter:
        profiles = profiles.filter(city=city_filter)
    if type_filter:
        profiles = profiles.filter(type=type_filter)
    if dimensions_filter:
        profiles = profiles.filter(dimensions__lte=dimensions_filter)
    if price_filter:
        profiles = profiles.filter(price__lte=price_filter)  # Filter profiles with price less than or equal to the specified price
    
    context = {
        'cities': cities,
        'profile': profiles,
    }
    
    return render(request, 'jyore/MarketPlace.html', context)









def sell(request):
    if request.method == 'POST':
        user = request.user  # Get the User instance
        Landlord_Name = request.POST['username']
        price = request.POST['price']
        email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        dimensions = request.POST['dimensions']
        mainimage = request.FILES.get('mainimage')
        subimage1 = request.FILES.get('subimage1')
        subimage2 = request.FILES.get('subimage2')
        subimage3 = request.FILES.get('subimage3')
        type_of_property = request.POST["type_of_property"]
        
        try:
            profile = Profile(
                user=user,  # Assign the User instance to the user field
                Landlord_Name=Landlord_Name,
                price=price,
                email=email,
                mobile=mobile,
                address=address,
                city=city,
                state=state,
                dimensions=dimensions,
                mainimage=mainimage,
                subimage1=subimage1,
                subimage2=subimage2,
                subimage3=subimage3,
                type_of_property=type_of_property
            )
            
            # Perform model validation
            profile.save()
            
            messages.success(request, 'Profile created successfully.')
            return redirect('marketplace')
        except Exception as e:
            return HttpResponse(e)
    
    return render(request, 'jyore/sell.html')
