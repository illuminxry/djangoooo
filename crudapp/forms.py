from django import forms
from crudapp.models import Student, Attendance

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'section', 'department','age','gender','address', 'studentnumber']
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'section': forms.TextInput(attrs={ 'class': 'form-control' }),
            'department': forms.TextInput(attrs={ 'class': 'form-control' }),
            'age': forms.TextInput(attrs={ 'class': 'form-control' }),
            'gender': forms.TextInput(attrs={ 'class': 'form-control' }),
            'address': forms.TextInput(attrs={ 'class': 'form-control' }),
            'studentnumber': forms.TextInput(attrs={ 'class': 'form-control' }),
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
        

class AttendanceForm(forms.ModelForm):
    status = forms.ChoiceField(widget=forms.RadioSelect, choices=Attendance.ATTENDANCE_CHOICES)

    class Meta:
        model = Attendance
        fields = ['status', 'student']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].widget.attrs['disabled'] = True