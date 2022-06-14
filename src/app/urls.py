from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^add-remember/$', views.add_remember, name='add-remember'),
]