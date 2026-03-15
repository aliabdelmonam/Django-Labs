from django.db import models
from utils.base_model import BaseModel
# Create your models here.

class Student(BaseModel):
    name = models.CharField(max_length=200)
    student_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    major = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='students/', blank=True, null=True)
    enrolled_date = models.DateField(auto_now_add=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']