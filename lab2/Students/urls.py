from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_students, name='list_students'),
    path('details/<int:pk>/', views.student_details, name='student_details'),
]

