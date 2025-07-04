from django.shortcuts import render, redirect, get_object_or_404

from studentsmgmt.models import Student


# Create your views here.
def students_list(request):
    students = Student.objects.all()
    return render(request,'studentsmgmt/students_list.html',{'students':students})

def student_create(request):
    if request.method == 'POST':
        roll_number =request.POST['roll_number' ]
        name = request.POST['name']
        age = request.POST['age']
        Student.objects.create(roll_number=roll_number,name=name,age=age)
        return redirect('students_list')
    return render(request,'studentsmgmt/student_form.html')

def student_update(request,roll_number):
    student = Student.objects.get(roll_number=roll_number)
    if request.method == 'POST':
        student.roll_number =request.POST['roll_number' ]
        student.name = request.POST['name']
        student.age = request.POST['age']
        student.save()
        return redirect('students_list')
    return render(request,'studentsmgmt/student_form.html')

def student_delete(request,roll_number):
    student = get_object_or_404(Student,roll_number=roll_number)
    if request.method == 'POST':
        student.delete()
        return redirect('students_list')
    return  render(request,'studentsmgmt/student_delete.html',{'student':student})