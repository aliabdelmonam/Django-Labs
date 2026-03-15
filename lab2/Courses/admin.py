from django.contrib import admin
from .models import Course

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'instructor', 'credits', 'capacity')
    search_fields = ('code', 'title')
    filter_horizontal = ('students',)
