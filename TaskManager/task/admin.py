from django.contrib import admin
from .models import *

class TaskInline(admin.TabularInline):
    model = Task
    extra = 0


class ReminderInlin(admin.TabularInline):
    model = Reminder
    extra = 0



@admin.register(TaskGroup)
class TaskGropeAdmin(admin.ModelAdmin):

    list_display = ['user', 'title', 'date']
    list_filter = ['date']
    raw_id_fields = ['user']

    inlines = [TaskInline]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = ['title', 'last_time', 'is_important', 'is_done', 'date']
    list_filter = ['is_important', 'is_done', 'date']
    raw_id_fields = ['group']

    inlines = [ReminderInlin]


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):

    list_display = ['title', 'reminder']
    raw_id_fields = ['task']

