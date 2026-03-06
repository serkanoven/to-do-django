
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views # Çıkış yapmak için hazır view

urlpatterns = [
    path('', views.index, name='list'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='register'), name='logout'), # Çıkış yapınca register'a at
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('complete/<int:pk>/', views.complete_task, name='complete_task'),
]