from django import forms
from .models import *

class CreateTaskGroup(forms.ModelForm):
    class Meta:
        model = TaskGroup
        fields = ['title']


class CreateTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'info', 'last_time', 'is_important']


class CreateReminder(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'reminder']


class EmailCover(forms.Form):
    full_name = forms.CharField(max_length= 70, label= 'نام کامل شما', required= True)
    email = forms.EmailField(max_length= 50, label= 'ایمیل شما', required= True)
    subject = forms.CharField(max_length= 50, label= 'عنوان پیام', required= True)
    message = forms.CharField(widget= forms.Textarea, label= 'متن پیام', required= True)