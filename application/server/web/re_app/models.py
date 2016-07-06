#!/usr/bin/env python
# -*- coding: UTF-8 -*- 


from django.db import models
from datetime import datetime

class City(models.Model):
    name = models.CharField(u'Город', unique=True, max_length=30)
	 
    def __unicode__(self):
	return self.name  

    class Meta:
        managed = True
	verbose_name = u'Город'
        verbose_name_plural = u'города'
	db_table = 'cities'


class Street(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name = 'Город')
    name = models.CharField(u'Улица', max_length=100)

    def __unicode__(self):
        return self.city.name + ', '+ self.name

    class Meta:
        managed = True
        verbose_name = u'Улица'
        verbose_name_plural = u'улицы'
        db_table = 'streets'
	

class TrashStation(models.Model):
    trash_type = models.ForeignKey('TrashType', on_delete=models.CASCADE, verbose_name = 'Тип отходов')
    station = models.ForeignKey('Station', on_delete=models.CASCADE, verbose_name = 'Станция утилизации')

    def __unicode__(self):
        return 'Trash-Station'
   
    class Meta:
        managed = True
        verbose_name = u'объект'
        verbose_name_plural = u'объекты'
	db_table = 'trash-stations'


class Station(models.Model):
    DAYS_OF_WEEK = (
        (u'Пн', u'Понедельник'),
	(u'Вт', u'Вторник'),
	(u'Ср', u'Среда'),
	(u'Чт', u'Четверг'),
	(u'Пт', u'Пятница'),
	(u'Сб', u'Суббота'),
	(u'Вс', u'Воскресение')
    )

    name = models.CharField(u'Станция', max_length=30)
    telephone = models.CharField(u'Телефон', max_length=20, null =True)
    day_open = models.CharField(u'Работает с', max_length=2, choices=DAYS_OF_WEEK, default=u'Пн')
    day_close = models.CharField(u'по', max_length=2, choices=DAYS_OF_WEEK, default=u'Сб')
    time_open = models.TimeField(u'Открывается в', blank=True, null = True)
    time_close = models.TimeField(u'Закрываеться в', blank=True, null = True)
    street = models.ForeignKey(Street, on_delete=models.CASCADE, verbose_name = 'Улица')
    house = models.SmallIntegerField(u'Дом')
    building = models.SmallIntegerField(u'Корпус', blank=True,null=True)
    raiting = models.SmallIntegerField(u'Рэйтинг', blank=True, default = 0)
    nof_use = models.IntegerField(u'Популярность', default = 0) 
    position_x = models.FloatField(u'Широта', blank=True,null=True)
    position_y = models.FloatField(u'Долгота', blank=True,null=True)
    add_date = models.DateTimeField(u'Дата добавления', auto_now_add=True)
    update_date = models.DateTimeField(u'Дата обновления', auto_now=True)
    description = models.TextField(u'Описание', blank=True, null=True)
    show = models.BooleanField(u'На карте', default=False)


    def __unicode__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = u'Станция утилизации отходов'
        verbose_name_plural = u'cтанции утилизации'
        db_table = 'stations'


class TrashClass(models.Model):
    name = models.CharField(u'Класс отходов', max_length=30)
    description = models.TextField(u'Описание', blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        managed = True        
	verbose_name = u'Класс отходов'
        verbose_name_plural = u'классы отходов'
        db_table = 'trash_classes'


class Trash(models.Model):
    name = models.CharField(u'Название', max_length=30)
    type = models.ForeignKey('TrashType', on_delete=models.CASCADE, verbose_name = 'Тип')
    class_id = models.ForeignKey('TrashClass', on_delete=models.CASCADE, verbose_name = 'Класс') 

    def __unicode__(self):
        return self.name

    class Meta:
        managed = True
	verbose_name = u'Утиль'
        verbose_name_plural = u'утиль'
        db_table = 'trash'


class TrashType(models.Model):
    name = models.CharField(u'Тип', unique=True, max_length=30)
    description = models.TextField(u'Описание', blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = u'Тип отходов'
        verbose_name_plural = u'типы отходов'
        db_table = 'trash_types'


class User(models.Model):
    login = models.CharField(u'Логин', unique=True, max_length=30)
    password = models.BigIntegerField(u'Пароль', unique=True)
    reg_date = models.DateField(u'Дата регистрации', auto_now_add=True)
    raiting = models.IntegerField(u'Уровень')

    def __unicode__(self):
        return self.login

    class Meta:
        managed = True
        verbose_name = u'Пользователь'
        verbose_name_plural = u'пользователи'
        db_table = 'users'


class UserTrash(models.Model):
    trash = models.ForeignKey(Trash, on_delete=models.CASCADE, verbose_name=u'Утиль')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u'Пользователь')

    def __unicode__(self):
        return 'User-Trash'

    class Meta:
        managed = True
        verbose_name = u'объект'
        verbose_name_plural = 'объекты'
        db_table = 'users-trash'


class VkUser(models.Model):
    address = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = True
        db_table = 'vk_users'

class FacebookUser(models.Model):
    address = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = True
        db_table = 'facebook_users'

class UserSocialnet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vk = models.ForeignKey(VkUser, on_delete=models.CASCADE)
    facebook = models.ForeignKey(FacebookUser, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'user-socialnet'

