from django.contrib import admin
from .models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_id', 'email', 'major', 'gpa', 'enrolled_date')
    list_filter = ('major', 'enrolled_date')
    search_fields = ('name', 'student_id', 'email')
    readonly_fields = ('enrolled_date',)
