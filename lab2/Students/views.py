from django.shortcuts import render
from .models import Student

# Create your views here.

def list_students(request):
    students = Student.objects.all()
    return render(request, 'student/list.html', {'students': students})

def student_details(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'student/details.html', {'student': student})
