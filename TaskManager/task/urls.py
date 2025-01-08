from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.menu, name= 'menu'),
    path('order_task/', views.order_task, name= 'order_task'),
    path('create_group/', views.create_group, name= 'create_group'),
    path('del_group/<int:id>', views.del_group, name= 'del_group'),
    path('edit_group/<int:id>', views.edit_group, name= 'edit_group'),
    path('create_task/<int:id>', views.create_task, name= 'create_task'),
    path('group_info/<int:id>', views.group_info, name= 'group_info'),
    path('del_task/<int:id>/<int:g_id>', views.del_task, name= 'del_task'),
    path('edit_task/<int:id>/<int:g_id>', views.edit_task, name= 'edit_task'),
    path('create_reminder/<int:id>/<int:g_id>', views.create_reminder, name='create_reminder'),
    path('task_reminders/<int:id>', views.task_reminders, name= 'task_reminders'),
    path('del_reminder/<int:id>/<int:t_id>', views.del_reminder, name= 'del_reminder'),
    path('edit_reminder/<int:id>/<int:t_id>', views.edit_reminder, name= 'edit_reminder'),
    path('check_box/', views.check_box, name= 'check_box'),
    path('cover/', views.cover, name= 'cover'),
    path('alarm/', views.alarm, name= 'alarm')
]