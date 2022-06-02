from django.contrib import admin

from classifiers import models


@admin.register(models.University)
class UniversityAdmin(admin.ModelAdmin):
    date_hierarchy = 'added_time'
    list_display = [
        'id',
        'name',
        'added_time',
        'last_updated_time',
    ]
    search_fields = [
        'name',
    ]
    readonly_fields = [
        'added_time',
        'last_updated_time',
    ]


@admin.register(models.Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    date_hierarchy = 'added_time'
    list_display = [
        'id',
        'name',
        'added_time',
        'last_updated_time',
    ]
    search_fields = [
        'name',
    ]
    readonly_fields = [
        'added_time',
        'last_updated_time',
    ]


@admin.register(models.Passion)
class PassionAdmin(admin.ModelAdmin):
    date_hierarchy = 'added_time'
    list_display = [
        'id',
        'name',
        'added_time',
        'last_updated_time',
    ]
    search_fields = [
        'name',
    ]
    readonly_fields = [
        'added_time',
        'last_updated_time',
    ]


@admin.register(models.Position)
class PositionAdmin(admin.ModelAdmin):
    date_hierarchy = 'added_time'
    list_display = [
        'id',
        'name',
        'added_time',
        'last_updated_time',
    ]
    search_fields = [
        'name',
    ]
    readonly_fields = [
        'added_time',
        'last_updated_time',
    ]
