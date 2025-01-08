from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import TaskGroup, Task
from .forms import *
from account.decorators import uniq_model, check_task
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from datetime import datetime
import jdatetime


def menu(request):
    return render(request, 'prim/menu.html')


@login_required
def order_task(request):
    task_groups = TaskGroup.objects.filter(user= request.user)
    return render(request, 'prim/order_task.html', {'task_groups': task_groups})



@uniq_model(TaskGroup)
@login_required
def create_group(request):
    
    if request.method == 'POST':
        form = CreateTaskGroup(request.POST)

        if form.is_valid():
            group = form.save(commit= False)
            group.user = request.user
            group.save()
            return redirect('task:order_task')
    
    else:
        form = CreateTaskGroup()
    
    return render(request, 'prim/create_group.html', {'form': form})


@login_required
def del_group(request, id):
    TaskGroup.objects.get(id= id).delete()
    return redirect('task:order_task')


@uniq_model(TaskGroup)
@login_required
def edit_group(request, id):
    group = TaskGroup.objects.get(id= id)

    if request.method == 'POST':
        form = CreateTaskGroup(request.POST, instance= group)

        if form.is_valid():
            new_group = form.save()
            new_group.save()
            return redirect('task:order_task')
    
    else:
        form = CreateTaskGroup(instance= group)
    
    return render(request, 'prim/edit_group.html', {'form': form})


@uniq_model(Task)
@login_required
def create_task(request, id):
    group = TaskGroup.objects.get(id= id)

    if request.method == 'POST':
        form = CreateTask(request.POST)

        if form.is_valid():
            task = form.save(commit= False)
            task.group = group
            task.save()
            return redirect('task:order_task')
    
    else:
        form = CreateTask()
    
    return render(request, 'prim/create_task.html', {'form': form, 'group': group})


@check_task
@login_required
def group_info(request, id):
    group = TaskGroup.objects.get(id= id)
    tasks = Task.objects.filter(group= group)
    return render(request, 'prim/group_info.html', {'tasks': tasks, 'group': group})


@login_required
def del_task(request, id, g_id):
    task = Task.objects.get(id= id)
    task.delete()
    return redirect('task:group_info', id= g_id)


@uniq_model(Task)
@login_required
def edit_task(request, id, g_id):
    task = Task.objects.get(id= id)

    if request.method == 'POST':
        form = CreateTask(request.POST, instance= task)

        if form.is_valid():
            new_task = form.save()
            new_task.save()
            return redirect('task:group_info', id= g_id)
    
    else:
        form = CreateTask(instance= task)
    
    return render(request, 'prim/edit_task.html', {'form': form, 'task': task})



@uniq_model(Reminder)
@login_required
def create_reminder(request, id, g_id):
    task = Task.objects.get(id= id)

    if request.method == 'POST':
        form = CreateReminder(request.POST)

        if form.is_valid():
            reminder = form.save(commit= False)
            reminder.task = task
            reminder.save()
            return redirect('task:group_info', id= g_id)
    
    else:
        form = CreateReminder()
    
    return render(request, 'prim/create_reminder.html', {'form': form, 'task': task})


@login_required
def task_reminders(request, id):
    task = Task.objects.get(id= id)
    reminders = Reminder.objects.filter(task= task)
    return render(request, 'prim/task_reminders.html', {'reminders': reminders, 'task': task})


@login_required
def del_reminder(request, id, t_id):
    reminder = Reminder.objects.get(id= id)
    reminder.delete()
    return redirect('task:task_reminders', id= t_id)



@uniq_model(Reminder)
@login_required
def edit_reminder(request, id, t_id):
    reminder = Reminder.objects.get(id= id)

    if request.method == 'POST':
        form = CreateReminder(request.POST, instance= reminder)
        
        if form.is_valid():
            new_reminder = form.save()
            new_reminder.save()
            return redirect('task:task_reminders', id= t_id)
        
    else:
        form = CreateReminder(instance= reminder)
    
    return render(request, 'prim/create_reminder.html', {'form': form, 'task': Task.objects.get(id= t_id)})



@require_POST
@login_required
def check_box(request):
    task_id = request.POST.get('task_id')
    task = Task.objects.get(id= task_id)

    if task.is_miss:
        data = {}
        return JsonResponse(data)

    elif task.is_done:
        task.is_done = False
    
    else:
        task.is_done = True
    
    task.save()


    data = {'is_done': 'شده' if task.is_done else 'نشده'}
    
    return JsonResponse(data)


def cover(request):

    sent = False
    
    if request.method == 'POST':
        form = EmailCover(request.POST)

        if form.is_valid():
            message = f'{form.cleaned_data["full_name"]} - {form.cleaned_data["email"]}:\n{form.cleaned_data["message"]}'
            send_mail(form.cleaned_data['subject'], message, 'manizero20@gmail.com', ['manirazeghi049@gmail.com'], fail_silently= True)
            sent = True

    else:
        form = EmailCover()
    
    return render(request, 'prim/cover.html', {'form': form, 'sent': sent})


@login_required
def alarm(request):
    now_time_list = datetime.today().strftime('%Y-%m-%d').split('-')
    now_time = jdatetime.date.fromgregorian(day= int(now_time_list[2]), month= int(now_time_list[1]), year= int(now_time_list[0]))
    
    targets = Reminder.objects.filter(task__group__user = request.user).filter(reminder= str(now_time))

    return render(request, 'prim/alarm.html', {'targets': targets, 'now_time': now_time})