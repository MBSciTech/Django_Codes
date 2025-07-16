from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from .models import Student
from .forms import StudentForm

def student_list(request) : 
    students = Student.objects.all()
    return render(request,'student_list.html',{'students':students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid() :
            form.save()
            redirect('student_list.html')
    else:
        form = StudentForm()

    return render(request,'student_create.html',{'form':form})


def student_update(request,pk):
    student = get_object_or_404(Student,pk = pk)
    form = StudentForm(request.POST or None,instance=student)
    if form.is_valid():
        form.save()
        return redirect('student')
    return render(request,'student_create.html',{'form':form})

def student_delete(request,pk):
    student = get_object_or_404(Student,pk = pk)
    form = StudentForm(request.POST or None,instance=student)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request,'student_delete.html',{'student':student})