from admin_auto_filters.filters import AutocompleteFilter
from django.contrib import admin

from students import models


class PositionFilter(AutocompleteFilter):
    title = 'Position'
    field_name = 'position'


class StudentFilter(AutocompleteFilter):
    title = 'Student'
    field_name = 'student'


class EducationTabularInline(admin.TabularInline):
    model = models.Education
    extra = 0
    fields = [
        'university',
        'speciality',
        'start_year',
        'graduate_year',
    ]
    readonly_fields = [
        'added_time',
        'last_updated_time',
    ]
    autocomplete_fields = [
        'university',
        'speciality',
    ]


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    date_hierarchy = 'added_time'
    list_display = [
        'id',
        'first_name',
        'last_name',
        'middle_name',
        'username',
        'photo',
        'birth_date',
        'gender',
        'address',
        'position',
        'views_count',
        'is_active',
        'added_time',
        'last_updated_time',
    ]
    list_filter = [
        'is_active',
        'gender',
        PositionFilter,
    ]
    search_fields = [
        'first_name',
        'last_name',
        'middle_name',
        'username',
        'address',
    ]
    inlines = [
        EducationTabularInline,
    ]
    filter_horizontal = [
        'passions',
    ]
    autocomplete_fields = [
        'position',
    ]
    readonly_fields = [
        'views_count',
        'added_time',
        'last_updated_time',
    ]


@admin.register(models.Achievement)
class AchievementAdmin(admin.ModelAdmin):
    date_hierarchy = 'added_time'
    list_display = [
        'id',
        'student',
        'title',
        'description',
        'date',
        'added_time',
        'last_updated_time',
    ]
    list_filter = [
        StudentFilter,
    ]
    search_fields = [
        'title',
        'description',
    ]
    autocomplete_fields = [
        'student',
    ]
    readonly_fields = [
        'added_time',
        'last_updated_time',
    ]


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'added_time'
    list_display = [
        'id',
        'student',
        'title',
        'description',
        'body',
        'added_time',
        'last_updated_time',
    ]
    list_filter = [
        StudentFilter,
    ]
    search_fields = [
        'title',
        'description',
    ]
    autocomplete_fields = [
        'student',
    ]
    readonly_fields = [
        'added_time',
        'last_updated_time',
    ]
