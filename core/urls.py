from django.contrib import admin
from django.urls import path
from django.urls import include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Portafolio.urls'))
]
