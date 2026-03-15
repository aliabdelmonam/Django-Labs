from django.db import models
from utils.base_model import BaseModel

# Create your models here.
class Course(BaseModel):
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    credits = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    instructor = models.ForeignKey(
        'Instrcutor.Instructor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='courses'
    )
    students = models.ManyToManyField(
        'Students.Student',
        blank=True,
        related_name='courses'
    )

    def __str__(self):
        return f"{self.code} - {self.title}"
    
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'