from django.shortcuts import render, redirect

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

