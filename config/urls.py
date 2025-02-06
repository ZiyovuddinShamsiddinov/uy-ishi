from django.contrib import admin
from django.urls import path,include
from config1.views import a
from config1.views import b
from config1.views import c
from config2.views import d
from config2.views import e
from config2.views import f
from config3.views import g
from config3.views import h
from config3.views import i


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('birinchi.birinchi/', a),
    # path('birinchi.ikkinchi/', b),
    # path('birinchi.uchisi/', c),
    # path('ikkinchisi.birinchi/', d),
    # path('ikkinchisi.ikkinchi/', e),
    # path('ikkinchisi.uchinchisi/', f),
    # path('uchinchisi.birinchi/', g),
    # path('uchinchisi.ikkinchi/', h),
    # path('uchinchisi.uchinchisi/', i),
    path('config1/',include('config1.urls')),
    path('config2/', include('config2.urls')),
    path('config3/', include('config3.urls'))

]
