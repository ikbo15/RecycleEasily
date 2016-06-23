# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Cities(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'cities'


class FacebookUsers(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    address = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'facebook_users'


class StationExamples(models.Model):
    trash = models.ForeignKey('Stations', models.DO_NOTHING)
    station = models.ForeignKey('TrashExamples', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'station-examples'


class StationTypes(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=30)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'station_types'


class Stations(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=30)
    street = models.ForeignKey('Streets', models.DO_NOTHING)
    house = models.SmallIntegerField()
    building = models.SmallIntegerField(blank=True, null=True)
    type = models.ForeignKey(StationTypes, models.DO_NOTHING)
    raiting = models.SmallIntegerField(blank=True, null=True)
    position_x = models.FloatField(blank=True, null=True)
    position_y = models.FloatField(blank=True, null=True)
    add_date = models.DateField()
    update_date = models.DateField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stations'


class Streets(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    city = models.ForeignKey(Cities, models.DO_NOTHING)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'streets'


class TrashClasses(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=30)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'trash_classes'


class TrashExamples(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=30)
    type = models.ForeignKey('TrashTypes', models.DO_NOTHING)
    class_field = models.ForeignKey(TrashClasses, models.DO_NOTHING, db_column='class_id')  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'trash_examples'


class TrashTypes(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=30)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'trash_types'


class UserSocialnet(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, primary_key=True)
    vk = models.ForeignKey('VkUsers', models.DO_NOTHING)
    facebook = models.ForeignKey(FacebookUsers, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user-socialnet'


class Users(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    login = models.CharField(unique=True, max_length=30)
    password = models.BigIntegerField(unique=True)
    reg_date = models.DateField()
    raiting = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'


class UsersExamples(models.Model):
    trash = models.ForeignKey(TrashExamples, models.DO_NOTHING)
    user = models.ForeignKey(Users, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users-examples'


class VkUsers(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    address = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'vk_users'
