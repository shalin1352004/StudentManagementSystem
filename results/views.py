from django.shortcuts import render
from .models import Result  # Assuming the model is named Result

def result_view(request):
    StudentResult = Result.objects.all()
    return render(request, 'result.html', {'StudentResult': StudentResult})
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from student.models import Student

@login_required(login_url='login')
def add_result(request):
    if request.method == 'POST':
        roll_no = request.POST.get('RollNo')  # This should match enrollmentNo
        sub1 = request.POST.get('marksofsub1')
        sub2 = request.POST.get('marksofsub2')
        sub3 = request.POST.get('marksofsub3')
        sub4 = request.POST.get('marksofsub4')

        try:
            # ✅ Check if student with this enrollmentNo exists
            student = Student.objects.get(enrollmentNo=roll_no)

            # ✅ Prevent duplicate result entry
            if Result.objects.filter(RollNo=roll_no).exists():
                messages.error(request, f"Result already exists for Roll No: {roll_no}.")
            else:
                Result.objects.create(
                    RollNo=roll_no,
                    student_name=student.name,
                    marksofsub1=int(sub1),
                    marksofsub2=int(sub2),
                    marksofsub3=int(sub3),
                    marksofsub4=int(sub4)
                )
                messages.success(request, f"Result added successfully for {student.name}!")
                return redirect('add_result')

        except Student.DoesNotExist:
            messages.error(request, f"No student found with Enrollment No: {roll_no}.")

        except ValueError:
            messages.error(request, "Please enter valid numeric marks.")

    return render(request, 'add_result.html')
from django.shortcuts import render, get_object_or_404
from .models import Result

def result_detail(request, rollno):
    student = get_object_or_404(Result, RollNo=rollno)
    all_students = Result.objects.all().order_by('-marksofsub1', '-marksofsub2', '-marksofsub3', '-marksofsub4')

    # Calculate rank based on TotalMarks
    sorted_students = sorted(all_students, key=lambda x: x.TotalMarks, reverse=True)
    rank = sorted_students.index(student) + 1

    percentage = round((student.TotalMarks / 400) * 100, 2)

    return render(request, 'result_detail.html', {
        'student': student,
        'rank': rank,
        'percentage': percentage,
    })




