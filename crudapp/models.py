from django.db import models

# Create your models here.

class Student(models.Model):
    studentnumber = models.TextField(max_length=20, default='')
    name = models.TextField(max_length=65, default='')
    section = models.TextField(max_length=20, default='')
    department = models.TextField(max_length=20, default='')
    age = models.TextField(max_length=20, default='')
    gender = models.TextField(max_length=20, default='')
    address = models.TextField(max_length=100, default='')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.name
    
    
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status_choices = [
        ('Present', 'Present'),
        ('Late', 'Late'),
        ('Absent', 'Absent'),
    ]
    status = models.CharField(choices=status_choices, max_length=10)


    