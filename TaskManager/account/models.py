from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


class Manager(UserManager):

    def save_user(self, username, password= None, **extra):
        if username == None or password == None:
            raise ValueError(f'username and password must be set.\nget username: {username}.\npassword: {password}')
        
        user = self.model(username, extra)
        user.set_password(password)
        user.save(using= self._db)
        return user


    def save_superuser(self, username, password = None, **extra):
        extra.setdefault('is_superuser', True)
        extra.setdefault('is_staff', True)

        if extra.get('is_superuser') != True:
            raise ValueError('is_superuser must be True!')
        
        if extra.get('is_staff') != True:
            raise ValueError('is_staff must be True!')
        
        return self.save_user(username, password, extra)
    


class User(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(max_length= 20, verbose_name= 'نام کاربری', unique= True)
    email = models.EmailField(max_length= 50, verbose_name= 'ایمیل', unique= True)

    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default= False)

    objects = Manager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    class Meta:
        verbose_name = 'اکانت کاربری'
        verbose_name_plural = 'اکانت های کاربری'
   

    def __str__(self):
        return self.username
    





