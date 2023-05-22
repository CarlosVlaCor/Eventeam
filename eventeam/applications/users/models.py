from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )

    class Type(models.IntegerChoices):
        SUPER_ADMIN = (0, 'Super Admin')
        USER = (1, 'user')
        CLIENT = (2, 'Client')

    type = models.IntegerField(verbose_name='Type', choices=Type.choices)
    first_name = models.CharField(verbose_name='Nombre', max_length=100)
    last_name = models.CharField(verbose_name='Apellidos', max_length=100)
    region = models.CharField(verbose_name='Region', max_length=50)
    city = models.CharField(verbose_name='Ciudad', max_length=50)
    phone = models.CharField(verbose_name='Celular', max_length=20)
    email = models.EmailField(verbose_name='Email', unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
