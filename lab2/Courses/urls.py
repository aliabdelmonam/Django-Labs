from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_courses, name='list_courses'),
    path('details/<int:pk>/', views.course_details, name='course_details'),
    path('instructor/<int:instructor_pk>/', views.instructor_courses, name='instructor_courses'),
]
