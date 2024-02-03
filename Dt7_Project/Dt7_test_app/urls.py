from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home_view),
    path('contact/', Contact_Us_View,name='contact'),

]