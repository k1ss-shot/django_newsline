from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from apps.users.manager import UserManager

class User(AbstractBaseUser, PermissionsMixin):

    nickname = models.CharField(verbose_name='Никнейм', max_length=255)
    email = models.EmailField(verbose_name='Почта', unique=True)
    is_active = models.BooleanField(verbose_name='Активный', default=True)
    is_staff = models.BooleanField(verbose_name='Сотрудник', default=False)
    date_joined = models.DateTimeField(
        verbose_name='Зарегестрирован', default=timezone.now,
    )

    USERNAME_FIELD = 'email'
    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.nickname
