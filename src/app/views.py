from django.shortcuts import render
from django.views import generic
from django.shortcuts import render
from django.utils import timezone

from .models import User, Remember

# Create your views here.

def index(request):    
    user = request.user
    if request.user.is_authenticated:
        print(user.email)
        print(user.get_full_name())
        full_name = user.get_full_name()
        username = user.username
        remembers = Remember.objects.filter(author=username)
        return render(request, 
            'app/remember_list.html',
            context={'remember_list': remembers, 'name': full_name})
    else:
        return render(request, 'auth.html', context={})

def add_remember(request):    
    user = request.user
    if request.user.is_authenticated:
        full_name = user.get_full_name()
        username = user.username
        remembers = Remember.objects.filter(author=username)
        return render(request, 
            'app/remember_list.html',
            context={'remember_list': remembers, 'name': full_name})
    else:
        return render(request, 'auth.html', context={})