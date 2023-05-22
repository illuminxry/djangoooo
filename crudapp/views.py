from django.shortcuts import redirect, render
from .forms import StudentForm, AttendanceForm
from .models import Student, Attendance
from datetime import datetime
# Create your views here.

def index(request):
    students = Student.objects.all()
    return render(request,"index.html",{'students':students})

def userinfo(request):
    return render(request,"userinfo.html")
    # form = StudentForm(request.POST, request.FILES)
    # if form.is_valid():
    #     form.save()
    #     return redirect('/')
    
def create(request):

    if request.method == 'POST':
        studentnumber = request.POST.get('studentnumber')
        name = request.POST.get('name')
        section = request.POST.get('section')
        department = request.POST.get('department')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        profile_picture = request.FILES.get('profile_picture')
        
        student = Student(
            studentnumber=studentnumber,
            name=name,
            section=section,
            department=department,
            age=age,
            gender=gender,
            address=address,
            profile_picture=profile_picture
        )
        student.save()
        
        return redirect('/')
    
    return render(request, 'create.html')

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
    if request.method == 'POST':
        student_ids = request.POST.getlist('studentnumber')
        statuses = request.POST.getlist('status')
        dates = request.POST.getlist('date')
        subjects = request.POST.getlist('subjects')
        discussions = request.POST.getlist('discussion')
        rooms = request.POST.getlist('room')

        for student_id, status, date, subject, discussion, room in zip(student_ids, statuses, dates, subjects, discussions, rooms):
            try:
                student = Student.objects.get(studentnumber=student_id)
                if date:  # Check if date is not empty
                    parsed_date = datetime.strptime(date, '%Y-%m-%d').date()
                    attendance = Attendance(student=student, status=status, subjects=subject, date=parsed_date, discussion=discussion, room=room)
                    attendance.save()
            except Student.DoesNotExist:
                pass

        return redirect("/displayattendance")
def display_attendance(request):
    attendance_data = Attendance.objects.select_related('student').all()
    context = {'attendance_data': attendance_data}
    return render(request, 'uploadattendance.html', context)
