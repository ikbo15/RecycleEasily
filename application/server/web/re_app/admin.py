#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.contrib import admin
from .models import *


class StreetAdmin(admin.ModelAdmin):
	list_display = ('name','city')

class TrashStationInLine(admin.StackedInline):
	model = TrashStation
	extra = 1
	verbose_name_plural = u'Типы принимаемых отходов'

class StationAdmin(admin.ModelAdmin):
	def display(modeladmin, request, queryset):
		queryset.update(show=True)

	def hide(modeladmin, request, queryset):
                queryset.update(show=False)

	display.short_description = u'Отобразить на карте'
	hide.short_description = u'Убрать с карты'
	actions = [display, hide]

        list_display = ('name', 'street', 'update_date', 'show')
	list_filter = ['street__city', 'show', 'add_date']
	search_fields = ['name']
	
	fieldsets = [
		(None, {'fields': ['name', 'description', 'show']}),
		(u'Адрес', {'fields': ['street', 'house', 'building']}),
	]
	inlines = [TrashStationInLine]	


class TrashAdmin(admin.ModelAdmin):
        list_display = ('name','type', 'class_id')

class UserTrashInLine(admin.StackedInline):
        model = UserTrash
        extra = 1
        verbose_name_plural = u'Утилизированные отходы'

class UserAdmin(admin.ModelAdmin):
        list_display = ('login', 'reg_date', 'raiting')
	inlines = [UserTrashInLine]

class TrashTypeAdmin(admin.ModelAdmin):
        list_display = ('name', 'description')

class TrashClassAdmin(admin.ModelAdmin):
        list_display = ('name', 'description')


admin.site.register(Station, StationAdmin)
#admin.site.register(City)
admin.site.register(Street, StreetAdmin)
admin.site.register(Trash, TrashAdmin)
admin.site.register(TrashType, TrashTypeAdmin)
admin.site.register(TrashClass, TrashClassAdmin)
admin.site.register(User, UserAdmin)
