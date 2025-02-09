from django.contrib import admin
from django.urls import path,include
from configapp.views import index
from configapp2.views import index2
from configapp3.views import index3


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('app/', index),
    # path('app2/', index2),
    # path('app3/', index3),
    path('app/', include('configapp.urls')),
    path('app2/', include('configapp2.urls')),
    path('app3/', include('configapp3.urls')),
]
