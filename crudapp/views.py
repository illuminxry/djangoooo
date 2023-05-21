from django.shortcuts import redirect, render
from .forms import StudentForm, AttendanceForm
from .models import Student, Attendance

# Create your views here.

def index(request):
    students = Student.objects.all()
    return render(request,"index.html",{'students':students})

def userinfo(request):
    return render(request,"userinfo.html")

def create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"create.html",{'form':form})

def view(request, id):  
    student = Student.objects.get(id=id)  
    return render(request,'view.html', {'student':student})

def edit(request, id):  
    student = Student.objects.get(id=id)  
    return render(request,'edit.html', {'student':student})  
 
def update(request, id):  
    student = Student.objects.get(id=id)  
    form = StudentForm(request.POST, instance = student)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'student': student})  

def delete(request, id):  
    student = Student.objects.get(id=id)  
    student.delete()  
    return redirect("/")

def attendance(request):
    students = Student.objects.all()
    return render(request,"attendance.html",{'students':students})  

def upload_attendance(request):
    students = Student.objects.all()  # Retrieve the list of students from your database

    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance')  # Redirect to a success page after successful form submission
    else:
        form = AttendanceForm()

    context = {
        'form': form,
        'students': students,
    }
    return render(request, 'uploadattendance.html', context)

