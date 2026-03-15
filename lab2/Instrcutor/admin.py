from django.contrib import admin
from .models import Instructor

# Register your models here.

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email', 'department', 'joined_date')
    list_filter = ('title', 'department', 'joined_date')
    search_fields = ('name', 'email')
    readonly_fields = ('joined_date',)
