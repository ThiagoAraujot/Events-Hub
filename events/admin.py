from django.contrib import admin
from .models import Employee, Events
# Register your models here.


class EventsAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'time', 'client_name', 'guests')
    list_filter = ['id', 'address', 'time', 'client_name', 'guests']


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'salary')
    list_filter = ['id', 'name', 'salary']


admin.site.register(Events, EventsAdmin)
admin.site.register(Employee, EmployeeAdmin)
