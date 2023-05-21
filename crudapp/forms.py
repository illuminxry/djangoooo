from django import forms
from crudapp.models import Student, Attendance

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'section', 'department','age','gender','address', 'studentnumber','profile_picture']
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'section': forms.TextInput(attrs={ 'class': 'form-control' }),
            'department': forms.TextInput(attrs={ 'class': 'form-control' }),
            'age': forms.TextInput(attrs={ 'class': 'form-control' }),
            'gender': forms.TextInput(attrs={ 'class': 'form-control' }),
            'address': forms.TextInput(attrs={ 'class': 'form-control' }),
            'studentnumber': forms.TextInput(attrs={ 'class': 'form-control' }),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
      }

# class AttendanceForm(forms.Form):
#     def __init__(self, *args, students=None, **kwargs):
#         super(AttendanceForm, self).__init__(*args, **kwargs)
#         if students:
#             for student in students:
#                 self.fields[f"attendance-{student.id}"] = forms.ChoiceField(
#                     choices=[("present", "Present"), ("late", "Late"), ("absent", "Absent")],
#                     widget=forms.RadioSelect(attrs={"class": "form-check-input"}),
#                     label=""
#                 )
#             self.students = students
        

# class AttendanceForm(forms.Form):
#     students = forms.ModelChoiceField(queryset=Student.objects.all())
#     status_choices = [
#         ('Present', 'Present'),
#         ('Late', 'Late'),
#         ('Absent', 'Absent'),
#     ]
#     status = forms.ChoiceField(choices=status_choices)

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
        }