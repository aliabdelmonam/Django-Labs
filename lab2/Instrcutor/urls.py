from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_instructors, name='list_instructors'),
    path('details/<int:pk>/', views.instructor_details, name='instructor_details'),
]
