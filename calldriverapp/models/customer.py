from typing import AbstractSet
from django.db import models
from .basemodels.basemodels import BaseModel

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


class MyUserManager(BaseUserManager):
    def create_user(self, username, password, phone_number, gear_type, **extra_fields):

        if not username:
            raise ValueError('must have user username')
       
        
        user = self.model(username=username, **extra_fields)
        user.gear_type = gear_type
        user.phone_number = phone_number
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('gear_type', 'auto')
        extra_fields.setdefault('phone_number', '0000')
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)

class MyUser(AbstractUser):
    email = None
    phone_number = models.CharField(max_length=50, null=True, blank= True)
    gear_type = models.CharField(max_length=50, choices=(('auto','자동'),('manual','수동')), default='auto')

    objects = MyUserManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'

    class Meta:
        db_table = "myuser"

    def __str__(self):
        return self.username