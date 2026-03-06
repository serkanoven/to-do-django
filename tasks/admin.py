from django.contrib import admin
from .models import Task # Kendi modelimizi içeri alıyoruz

admin.site.register(Task) # Admin paneline "bu modeli göster" diyoruz