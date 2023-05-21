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


    def __str__(self):
        return self.name
    
    
class Attendance(models.Model):
    ATTENDANCE_CHOICES = [
        ('present', 'Present'),
        ('late', 'Late'),
        ('absent', 'Absent'),
    ]

    status = models.CharField(max_length=10, choices=ATTENDANCE_CHOICES, default='')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default='')

    def __str__(self):
        return f"{self.student.name} - {self.status}"


    