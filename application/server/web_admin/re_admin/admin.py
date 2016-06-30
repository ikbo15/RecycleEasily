from django.contrib import admin
from .models import *


class StreetAdmin(admin.ModelAdmin):
	list_display = ('name','city')

class StationAdmin(admin.ModelAdmin):
        list_display = ('name', 'street','house', 'raiting', 'add_date', 'update_date')

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


