from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('universities.urls')),
    path('', include('programs.urls')),
    path('', include('services.urls')),
]
