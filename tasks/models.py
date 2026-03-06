from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200) # Görev başlığı (maksimum 200 karakter)
    completed = models.BooleanField(default=False) # Varsayılan olarak tamamlanmadı
    created_at = models.DateTimeField(auto_now_add=True) # Otomatik oluşturulma tarihi

    def __str__(self):
        return self.title