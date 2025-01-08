from functools import wraps
from django.http import HttpResponse
from task.models import *
from datetime import datetime
import jdatetime


def control_password(func):
    @wraps(func)
    def inner(request):

        if request.method == 'POST':
            password_inputer : str = request.POST.get('password')
            
            if len(password_inputer) < 6 or password_inputer.isdigit() or password_inputer.isalpha():
                return HttpResponse(f'weak password -> {password_inputer}\nthe password must have atleast 6 lengh\nand mix of numbers and letters.')
            
        return func(request)
    
    return inner


def uniq_model(model: TaskGroup|Task|Reminder):
    def decor(func):
        @wraps(func)
        def inner(*args, **kwargs):

            if args[0].method == 'POST':
               
               if model == Reminder:
                   timer = args[0].POST.get('reminder')

                   if model.objects.filter(reminder= timer):
                      return HttpResponse(f'{timer} را قبلا ساخته اید. لطفا یک زمان دیگر انتخاب کنید')


               else:
                   title = args[0].POST.get('title')

                   if model.objects.filter(title= title):
                      return HttpResponse(f'{title} را قبلا ساخته اید. لطفا یک نام دیگر انتخاب کنید')
            
            return func(*args, **kwargs)
    
        return inner
    return decor



def check_task(func):
    @wraps(func)
    def inner(*args, **kwargs):

        now_time_list = datetime.today().strftime('%Y-%m-%d').split('-')
        now_time = jdatetime.date.fromgregorian(day= int(now_time_list[2]), month= int(now_time_list[1]), year= int(now_time_list[0]))

        for task in Task.objects.filter(group__user= args[0].user, last_time__lt = str(now_time)):
            task.is_miss = True
            task.save()
        
        return func(*args, **kwargs)
    
    return inner
        
        
