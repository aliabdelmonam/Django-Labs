from django.db import models
from utils.base_model import BaseModel
# Create your models here.

class Instructor(BaseModel):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, default='Professor')
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    department = models.CharField(max_length=200, blank=True)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']