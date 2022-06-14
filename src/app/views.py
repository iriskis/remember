from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import RememberForm
from .models import Remember, Userpic

# Create your views here.

def index(request):    
    user = request.user
    if request.user.is_authenticated:
        print(user.email)
        print(user.get_full_name())
        full_name = user.get_full_name()
        username = user.username
        remembers = Remember.objects.filter(author=username).order_by('-date')
        userpic = Userpic.objects.filter(username=username).first()
        pic = userpic.pic if userpic else None
            
        return render(request, 
            'app/remember_list.html',
            context={'remember_list': remembers, 'name': full_name, 'pic': pic})
    else:
        return render(request, 'auth.html', context={})

def add_remember(request):    
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        form = RememberForm(request.POST)
        if form.is_valid():
            remember = Remember()
            remember.author = request.user.username
            remember.title = form.cleaned_data['title']
            remember.comment = form.cleaned_data['comment']
            remember.date = form.cleaned_data['date']
            remember.save()
            return HttpResponseRedirect('/')
    else:
        form = RememberForm()
        return render(request, 'form.html', {'form': form})



def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')