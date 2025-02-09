from django.contrib import admin
from django.urls import path
from configapp3.views import index3

urlpatterns = [

    path('index3/', index3)
]