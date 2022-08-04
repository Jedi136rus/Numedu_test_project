from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Storage(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название склада')

    def __str__(self):
        return self.name


class Staff(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=20, blank=False)
    last_name = models.CharField(verbose_name='Фамилия', max_length=20, blank=False)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE, related_name='storage', null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Machine(models.Model):
    maker = models.CharField(verbose_name='Производитель', max_length=200, null=False, blank=False)
    country = models.CharField(verbose_name='Страна', max_length=20, null=False, blank=False)
    type = models.CharField(verbose_name='Модель', max_length=200, null=False, blank=False)
    answerable = models.ForeignKey(Staff, verbose_name='Ответсвенный', on_delete=models.PROTECT, related_name='staff',
                                   null=False)

