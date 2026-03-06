from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse # BU SATIR EKSİK OLABİLİR, MUTLAKA EKLE
from django.contrib.auth.models import User

# Admin oluşturma fonksiyonu
def create_admin(request):
    try:
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'serkan123')
            return HttpResponse("Admin başarıyla oluşturuldu!")
        return HttpResponse("Admin zaten mevcut.")
    except Exception as e:
        return HttpResponse(f"Hata oluştu: {e}")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    path('gizli-admin-olustur/', create_admin), # Bu satırın sonundaki virgül önemli
]