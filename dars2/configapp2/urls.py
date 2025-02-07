from django.urls import path
from configapp2.views import index2

urlpatterns = [
    path('app2/', index2),
]