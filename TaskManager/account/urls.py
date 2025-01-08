from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('login_user/', auth_views.LoginView.as_view(), name= 'login_user'),
    path('profile/', views.profile, name= 'profile'),
    path('save_user/', views.save_user, name= 'save_user'),
    path('logout_user/', views.logout_user, name= 'logout_user'),
    path('edit_user/', views.edit_user, name= 'edit_user'),
    path('change_password/', auth_views.PasswordChangeView.as_view(success_url = 'done'), name= 'change_password'),
    path('change_password/done', auth_views.PasswordChangeDoneView.as_view(), name= 'password_change_done'),

    path('reset_password/', auth_views.PasswordResetView.as_view(success_url = 'done'), name= 'reset_password'),
    path('reset_password/done', auth_views.PasswordResetDoneView.as_view(), name= 'password_reset_done'),
    path('reset_password_confirm/<token>/<uidb64>', auth_views.PasswordResetConfirmView.as_view(success_url = '/reset_password/complete'), name= 'password_reset_confirm'),
    path('reset_password/complete', auth_views.PasswordResetCompleteView.as_view(), name= 'password_reset_complete'),
    path('task_analyse/', views.task_analyse, name= 'task_analyse')
]