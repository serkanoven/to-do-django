
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    # Önem derecesi seçenekleri
    PRIORITY_CHOICES = [
        ('low', 'Düşük'),
        ('medium', 'Orta'),
        ('high', 'Yüksek'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # YENİ ALANLAR:
    deadline = models.DateField(null=True, blank=True) # Son tarih
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium') # Önem sırası

    def __str__(self):
        return self.title