from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import *
from .decorators import control_password, check_task
from task.models import *


@login_required
def profile(request):
    return render(request, 'prim/profile.html')


@control_password
def save_user(request):
    
    if request.method == 'POST':
        form = SaveUserForm(request.POST)

        if form.is_valid():
            user = form.save(commit= False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('task:menu')
        
    else:
        form = SaveUserForm()
    
    return render(request, 'prim/save_user.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    return redirect('task:menu')


@login_required
def edit_user(request):

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance= request.user)

        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('account:profile')
        
    else:
        form = EditUserForm(instance= request.user)
    
    return render(request, 'prim/edit_user.html', {'form': form})


@check_task
@login_required
def task_analyse(request):
    user = request.user

    context = {
        'total_tasks': 0,
        'done_tasks': 0,
        'miss_tasks': 0,
        'feeds': 0
    }

    for gtask in TaskGroup.objects.filter(user= user):
        context['total_tasks'] += Task.objects.filter(group= gtask).count()
        context['done_tasks'] += Task.objects.filter(group= gtask, is_done= True).count()
        context['miss_tasks'] += Task.objects.filter(group= gtask, is_miss= True).count()
    
    context['feeds'] = context['done_tasks'] + context['miss_tasks']

    return render(request, 'prim/task_analyse.html', context= context)