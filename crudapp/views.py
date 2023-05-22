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

# def create(request):
#     form = StudentForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     return render(request,"create.html",{'form':form})
def create(request):
    form = StudentForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'create.html', context)

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

# def upload_attendance(request):
#     if request.method == 'POST':
#         form = AttendanceForm(request.POST)
#         if form.is_valid():
#             # date = form.cleaned_data['date']
#             student = form.cleaned_data['students']
#             status = form.cleaned_data['status']

#             attendance = Attendance(student=student, status=status)
#             attendance.save()

#             return redirect('success')  # Replace 'success' with the appropriate URL name for a success page

#     else:
#         form = AttendanceForm()

#     context = {'form': form}
#     return render(request, 'attendance.html', context)

# def upload_attendance(request):
#     if request.method == 'POST':
#         studentid = request.POST['studentnumber']
#         status = request.POST['status']

#         stud = Attendance(
#             student = studentid,
#             status = status
#         )
#         stud.save()
#         return redirect("/")

# def upload_attendance(request):
#     if request.method == 'POST':
#         studentid = request.POST['studentnumber']
#         status = request.POST['status']

#         student = Student.objects.get(studentnumber=studentid)  # Retrieve the student instance

#         attendance = Attendance(
#             student=student,  # Assign the student instance
#             status=status
#         )
#         attendance.save()

#         return redirect("/")
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
