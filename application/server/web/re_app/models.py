#!/usr/bin/env python
# -*- coding: UTF-8 -*- 


from django.db import models


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
        return self.name

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
        verbose_name = u'Утиль-Станция'
        verbose_name_plural = u'утиль-Станция'
	db_table = 'trash-stations'


class Station(models.Model):
    name = models.CharField(u'Станция', max_length=30)
    street = models.ForeignKey(Street, on_delete=models.CASCADE, verbose_name = 'Улица')
    house = models.SmallIntegerField(u'Дом')
    building = models.SmallIntegerField(u'Корпус', blank=True,null=True)
    raiting = models.SmallIntegerField(u'Популярность', blank=True,null=True)
    position_x = models.FloatField(u'Широта', blank=True,null=True)
    position_y = models.FloatField(u'Долгота', blank=True,null=True)
    add_date = models.DateField(u'Дата добавления')
    update_date = models.DateField(u'Дата обновления')
    description = models.TextField(u'Описание', blank=True, null=True)
    show = models.BooleanField(u'Видна на карте', default=False)


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
    reg_date = models.DateField(u'Дата регистрации')
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
        verbose_name = u'Пользователь-Утиль'
        verbose_name_plural = u'пользователь-Утиль'
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

