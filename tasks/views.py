from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required # BU SATIRIN OLDUĞUNDAN EMİN OL
from .models import Task

@login_required(login_url='/admin/login/') # HATAYI ÇÖZEN KRİTİK SATIR
def index(request):
    # --- YENİ GÖREV EKLEME ---
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

    # --- ARAMA VE LİSTELEME ---
    search_input = request.GET.get('search-area') or ''
    
    # Sadece giriş yapmış kullanıcının görevlerini getir
    tasks = Task.objects.filter(user=request.user)
    
    if search_input:
        tasks = tasks.filter(title__icontains=search_input)

    tasks = tasks.order_by('priority', '-created_at')
    
    return render(request, 'tasks/index.html', {'tasks': tasks, 'search_input': search_input})