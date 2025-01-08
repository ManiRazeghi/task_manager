from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserView(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_active', 'is_staff']


class UserCreate(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_active', 'is_staff']


class SaveUserForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput, label= 'رمز عبور')

    class Meta:
        model = User
        fields = ['username', 'email']


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']