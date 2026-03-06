from django.contrib import admin
from django.urls import path, include # include'u buraya ekledik

urlpatterns = [
    path('admin/', admin.site.urls), # Admin paneli adresi
    path('', include('tasks.urls')), # Ana sayfaya gelenleri 'tasks.urls'e gönderir
]
from django.contrib.auth.models import User

# BU SADECE BİR KEZ ÇALIŞTIRILIP SİLİNMELİDİR!
def create_admin(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'serkan123')
        return HttpResponse("Admin oluşturuldu!")
    return HttpResponse("Admin zaten var.")

# URL listesine ekle:
urlpatterns += [
    path('gizli-admin-olustur/', create_admin),
]