from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Task

# KAYIT OLMA FONKSİYONU (Hata buranın eksikliğinden kaynaklanıyor)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})

# ANA SAYFA (LİSTELEME)
@login_required(login_url='/admin/login/')
def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        deadline = request.POST.get('deadline')
        priority = request.POST.get('priority')
        
        if title:
            Task.objects.create(
                user=request.user, 
                title=title,
                deadline=deadline if deadline else None,
                priority=priority
            )
        return redirect('list')

    search_input = request.GET.get('search-area') or ''
    tasks = Task.objects.filter(user=request.user)
    
    if search_input:
        tasks = tasks.filter(title__icontains=search_input)

    tasks = tasks.order_by('priority', '-created_at')
    return render(request, 'tasks/index.html', {'tasks': tasks, 'search_input': search_input})

# GÖREV SİLME
@login_required(login_url='/admin/login/')
def delete_task(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    task.delete()
    return redirect('list')

# GÖREV TAMAMLAMA
@login_required(login_url='/admin/login/')
def complete_task(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('list')