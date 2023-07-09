from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from chat.models import Thread
from jyore.models import User




@login_required
def messages_page(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {
        'Threads': threads
    }
    return render(request, 'messages.html', context)

from django.shortcuts import redirect
from .models import Thread
from django.contrib import messages

@login_required
def create_thread(request, property_username):
    # Get the logged-in user and the property owner based on the usernames
    user = request.user
    property_owner = User.objects.get(first_name=property_username)
    if user == property_owner:
        redirect('marketplace')
    # Create the thread between the logged-in user and the property owner
    thread = Thread.objects.filter(first_person=user, second_person=property_owner).first()
    thread2 = Thread.objects.filter(first_person=property_owner, second_person=user).first()
    if thread:
        pass
    elif thread2:
        pass
    else:
         # Create a new thread
        thread = Thread.objects.create(first_person=user, second_person=property_owner)
        


    # Redirect to the messages page for the newly created thread
    return redirect('inbox')

