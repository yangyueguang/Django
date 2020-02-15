from django.contrib import admin
from apps.models.models import *


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_per_page = 10
    actions_on_top = True
    actions_on_bottom = True
    search_fields = ['name']
    list_filter = ['name', 'age']
    list_display = ['name', 'age', 'isDelete']




