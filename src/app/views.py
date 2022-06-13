from django.shortcuts import render

# Create your views here.
from .models import User, Remember

def index(request):
    num_users=User.objects.count()
    num_remebers=Remember.objects.count()  
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_users':num_users, 'num_remebers':num_remebers},
    )