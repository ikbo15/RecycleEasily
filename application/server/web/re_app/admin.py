#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.contrib import admin
from .models import *


class StreetAdmin(admin.ModelAdmin):
	list_display = ('name','city')

class StationAdmin(admin.ModelAdmin):
	def display(modeladmin, request, queryset):
		queryset.update(show=True)

	def hide(modeladmin, request, queryset):
                queryset.update(show=False)

	display.short_description = u'Отобразить на карте'
	hide.short_description = u'Убрать с карты'

	
	actions = [display, hide]
        list_display = ('name','get_city', 'street', 'update_date', 'show')
	list_filter = ['street__city', 'show', 'add_date']
	search_fields = ['name']
	def get_city(self,obj):
		return obj.street.city
	get_city.short_description = 'Город'

class TrashAdmin(admin.ModelAdmin):
        list_display = ('name','type', 'class_id')

class TrashStationAdmin(admin.ModelAdmin):
        list_display = ('trash_type', 'station')

class UserAdmin(admin.ModelAdmin):
        list_display = ('login', 'reg_date', 'raiting')

class UserTrashAdmin(admin.ModelAdmin):
        list_display = ('user', 'trash')

class TrashTypeAdmin(admin.ModelAdmin):
        list_display = ('name', 'description')

class TrashClassAdmin(admin.ModelAdmin):
        list_display = ('name', 'description')


admin.site.register(Station, StationAdmin)
admin.site.register(City)
admin.site.register(Street, StreetAdmin)
admin.site.register(Trash, TrashAdmin)
admin.site.register(TrashType, TrashTypeAdmin)
admin.site.register(TrashClass, TrashClassAdmin)
admin.site.register(TrashStation, TrashStationAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserTrash, UserTrashAdmin)

