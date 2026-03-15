from django.shortcuts import render
from .models import Instructor

# Create your views here.

def list_instructors(request):
    instructors = Instructor.objects.all()
    return render(request, 'instructor/list.html', {'instructors': instructors})

def instructor_details(request, pk):
    instructor = Instructor.objects.get(pk=pk)
    return render(request, 'instructor/details.html', {'instructor': instructor})
