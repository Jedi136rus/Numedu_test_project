from django.contrib import admin
from .models import Staff, Storage, Machine


class StorageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'storage')


class MachineAdmin(admin.ModelAdmin):
    list_display = ('id', 'maker', 'country', 'type', 'answerable')


admin.site.register(Staff, StaffAdmin)
admin.site.register(Storage, StorageAdmin)
admin.site.register(Machine, MachineAdmin)
