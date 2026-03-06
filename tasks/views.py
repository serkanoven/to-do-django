from django.shortcuts import render, redirect
from .models import Task

def index(request):
    # --- YENİ GÖREV EKLEME (POST İsteği) ---
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('list') # Sayfayı yenile

    # --- LİSTELEME ---
    tasks = Task.objects.all().order_by('-created_at') # Yeniler üstte
    return render(request, 'tasks/index.html', {'tasks': tasks})

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('list')

def complete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.completed = not task.completed # Durumu tersine çevir (Toggle)
    task.save()
    return redirect('list')