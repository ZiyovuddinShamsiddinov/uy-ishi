from django.contrib import admin
from django.urls import path,include
from configapp.views import index
from configapp2.views import index2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', index),
    path('app2/', index2),
]
