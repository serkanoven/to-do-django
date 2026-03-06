from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm # Hazır kayıt formu
from django.contrib.auth import login # Kayıttan sonra otomatik giriş için
from django.contrib.auth.decorators import login_required
from .models import Task

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # Kullanıcıyı kaydet
            login(request, user) # Otomatik giriş yap
            return redirect('list')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})

# ... diğer index, delete_task ve complete_task fonksiyonların aşağıda kalmaya devam etsin ...@login_required(login_url='/admin/login/')
def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(user=request.user, title=title)
        return redirect('list')

    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'tasks/index.html', {'tasks': tasks})

# Hatanın kaynağı buradaki eksiklikti:
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('list')

# Bunu da eklediğinden emin ol:
def complete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.completed = not task.completed
    task.save()
    return redirect('list')