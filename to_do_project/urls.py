from django.contrib import admin
from django.urls import path, include # include'u buraya ekledik

urlpatterns = [
    path('admin/', admin.site.urls), # Admin paneli adresi
    path('', include('tasks.urls')), # Ana sayfaya gelenleri 'tasks.urls'e gönderir
]