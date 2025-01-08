from django.db import models
from account.models import User


class TaskGroup(models.Model):
    # relation
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'task_groups', verbose_name= 'اکانت کاربری')

    title = models.CharField(max_length= 50, verbose_name= 'دسته بندی وظایف')
    date = models.DateTimeField(auto_now_add= True)

    class Meta:
        ordering = ['-date']

        indexes = [
            models.Index(fields= ['-date'])
        ]

        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
    
    def __str__(self):
        return self.title



class Task(models.Model):

    # relation
    group = models.ForeignKey(TaskGroup, on_delete= models.CASCADE, related_name= 'tasks', verbose_name= 'دسته بندی')

    # common
    title = models.CharField(max_length= 50, verbose_name= 'عنوان وظیفه')
    info = models.TextField(max_length= 300, verbose_name= 'توضیحات وظیفه')
    last_time = models.DateTimeField(auto_now_add= False, verbose_name= 'اتمام مهلت')
    is_important = models.BooleanField(default= False, verbose_name= 'آیا این وظیفه مهم شده')
    is_done = models.BooleanField(default= False, verbose_name= 'آیا وظیفه انجام شده')
    is_miss = models.BooleanField(default= False, verbose_name= 'آیا وظیفه فراموش شده')

    date = models.DateTimeField(auto_now_add= True, verbose_name= 'زمان ایجاد این وظیفه')

    class Meta:
        ordering = ['-date']

        indexes = [
            models.Index(fields= ['-date'])
        ]

        verbose_name = 'وظیفه'
        verbose_name_plural = 'وظایف'
    
    def __str__(self):
        return self.title



class Reminder(models.Model):
    # relation
    task = models.ForeignKey(Task, on_delete= models.CASCADE, related_name= 'reminders', verbose_name= 'وظیفه')

    # common
    reminder = models.DateTimeField(auto_now_add= False, verbose_name= 'یادآور')
    title = models.CharField(max_length= 50, verbose_name= 'متن یادآور')

    class Meta:

        verbose_name = 'یادآور'
        verbose_name_plural = 'یادآورها'
    
    def __str__(self):
        return f'{self.title}-{self.reminder}'
    
