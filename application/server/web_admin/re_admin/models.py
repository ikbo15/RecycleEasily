# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models


class City(models.Model):
    name = models.CharField(unique=True, max_length=30)
	 
    def __unicode__(self):
	return self.name  

    class Meta:
        managed = True
        verbose_name_plural = 'Cities'
	db_table = 'cities'


class Street(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'streets'
	

class TrashStation(models.Model):
    trash_type = models.ForeignKey('TrashType', on_delete=models.CASCADE)
    station = models.ForeignKey('Station', on_delete=models.CASCADE)

    def __unicode__(self):
        return 'Trash-Station connection'
   
    class Meta:
        managed = True
        verbose_name_plural = 'Trash-Stations'
	db_table = 'trash-stations'


class Station(models.Model):
    name = models.CharField(max_length=30)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    house = models.SmallIntegerField()
    building = models.SmallIntegerField(blank=True,null=True)
    raiting = models.SmallIntegerField(blank=True,null=True)
    position_x = models.FloatField(null=True)
    position_y = models.FloatField(null=True)
    add_date = models.DateField()
    update_date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'stations'


class TrashClass(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        managed = True
	verbose_name_plural = 'Trash classes'
        db_table = 'trash_classes'


class Trash(models.Model):
    name = models.CharField(max_length=30)
    type = models.ForeignKey('TrashType', on_delete=models.CASCADE)
    class_id = models.ForeignKey('TrashClass', on_delete=models.CASCADE, verbose_name='class') 

    def __unicode__(self):
        return self.name

    class Meta:
        managed = True
	verbose_name_plural = 'Trash'
        db_table = 'trash'


class TrashType(models.Model):
    name = models.CharField(unique=True, max_length=30)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'trash_types'


class User(models.Model):
    login = models.CharField(unique=True, max_length=30)
    password = models.BigIntegerField(unique=True)
    reg_date = models.DateField()
    raiting = models.IntegerField()

    def __unicode__(self):
        return self.login

    class Meta:
        managed = True
        db_table = 'users'


class UserTrash(models.Model):
    trash = models.ForeignKey(Trash, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return 'User-Trash connection'

    class Meta:
        managed = True
	verbose_name_plural = 'User-Trash'
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

