from django import forms
from crudapp.models import Student, Attendance

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'section', 'department','age','gender','address', 'studentnumber','profile_picture']
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            # 'section': forms.TextInput(attrs={ 'class': 'form-control' }),
            # 'department': forms.TextInput(attrs={ 'class': 'form-control' }),
            'age': forms.TextInput(attrs={ 'class': 'form-control' }),
            # 'gender': forms.TextInput(attrs={ 'class': 'form-control' }),
            'address': forms.TextInput(attrs={ 'class': 'form-control' }),
            'studentnumber': forms.TextInput(attrs={ 'class': 'form-control' }),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
      }
        
class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['status','date','subjects','discussion','room']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
        }