from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student
# Remove duplicate import of Student and Result
# from results.models import Result  # Only import if needed

# Student dashboard view
def student_dashboard(request):
    students = Student.objects.all()
    return render(request, 'student.html', {'students': students})

# Add student view
def add_student(request):
    if request.method == 'POST':
        enrollmentNo = request.POST.get('enrollmentNo')
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')

        # Check if enrollment or email already exists
        if Student.objects.filter(enrollmentNo=enrollmentNo).exists():
            messages.error(request, "Enrollment number already exists.")
        elif Student.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
        else:
            student = Student(
                enrollmentNo=enrollmentNo,
                name=name,
                age=age,
                email=email
            )
            student.save()
            messages.success(request, "Student added successfully!")
            return redirect('add_student')  # Redirect to form again or dashboard

    return render(request, 'add_student.html')
from .models import Student  # replace with your actual Student model
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def student_detail(request, enrollmentNo):
    student = get_object_or_404(Student, enrollmentNo=enrollmentNo)
    return render(request, 'student_detail.html', {'student': student})