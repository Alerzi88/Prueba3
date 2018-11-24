from django.urls import path
from . import views
from django.conf.urls import * 
from django.conf import settings
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.post_list, name='index'),
    path('galeria', views.galeria, name='galeria'),

]