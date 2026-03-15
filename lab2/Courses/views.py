from django.shortcuts import render, get_object_or_404
from .models import Course
from Instrcutor.models import Instructor
# Create your views here.
def list_courses(request):
    courses = Course.objects.all()
    return render(request,'courses/list.html',{'courses':courses})

def course_details(request,pk):
    course = Course.objects.get(pk=pk)
    return render(request,'courses/details.html',{'course':course})

def instructor_courses(request, instructor_pk):
    instructor = get_object_or_404(Instructor, pk=instructor_pk)
    courses = instructor.courses.all()
    if courses.exists():
        return render(request, 'courses/list.html', {'courses': courses})
    else:
        return render(request, 'courses/no_courses.html', {
            'message': 'This instructor PK is not linked to any course.'
        })
