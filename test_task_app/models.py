from django.contrib.auth.models import AbstractUser
from django.db import models


class Client(models.Model):
    account_number = models.PositiveBigIntegerField(verbose_name='Номер счета')
    surname = models.CharField(max_length=55, verbose_name='Фамилия')
    name = models.CharField(max_length=55, verbose_name='Имя')
    patronymic = models.CharField(max_length=55, verbose_name='Отчество', blank=True)
    date_birth = models.DateField(verbose_name='Дата рождения')
    inn = models.PositiveBigIntegerField(verbose_name='ИНН')
    STATUSES = (
        (0, 'Не в работе'),
        (1, 'Сделка закрыта'),
        (2, 'Отказ'),
        (3, 'В работе'),
    )
    status = models.PositiveSmallIntegerField(default=0, choices=STATUSES, verbose_name='Статус клиента')

    def __str__(self):
        return f'Клиент {self.name} - {self.surname}, \n Дата рождения {self.date_birth}, статус - {self.STATUSES[self.status]}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['name', 'surname']


class Person(AbstractUser):
    clients = models.ManyToManyField(to='Client', verbose_name='Клиенты')

    def __str__(self):
        return f'Пользователь {self.username}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username', ]
