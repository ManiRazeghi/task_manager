from django.contrib import admin
from .models import User
from .forms import UserView, UserCreate
from django.contrib.auth.admin import UserAdmin
from task.models import TaskGroup

class GroupInline(admin.TabularInline):
    model = TaskGroup
    extra = 0


@admin.register(User)
class UserAdmin(UserAdmin):

    ordering = ['username']

    list_display = ['username', 'email', 'is_superuser', 'is_active']
    list_editable = ['is_superuser', 'is_active']
    list_filter = ['is_superuser', 'is_active']

    model = User
    form = UserView
    add_form = UserCreate

    inlines = [GroupInline]


    fieldsets = (
        ('information', {'fields': ('username', 'email', 'is_superuser', 'is_active')}),
    )


    add_fieldsets = (
        ('information', {'fields': ('username', 'email', 'is_superuser', 'is_active', 'password1', 'password2')}),
    )
