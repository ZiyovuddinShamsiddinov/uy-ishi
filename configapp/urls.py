from django.urls import path
from .views import *
from configapp.views import Student

urlpatterns = [
    path('Student/',student),
    path('Kurs/',kurs),
]