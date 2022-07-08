from django.shortcuts import render, redirect
from app.forms import GradeForm, StudentCreationForm
from app.models import Student, Grade

def index(request):
    students = Student.objects.all()
    form = StudentCreationForm()
    context = { 'students': students, 'form': form }
    if request.method == "POST":
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'app/index.html', context)


def update_student_name(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentCreationForm(instance=student)
    context = { 'student': student, 'form': form }

    if request.method == "POST":
        form = StudentCreationForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'app/update_student_name.html', context)


def update_student_grade(request, pk):
    student = Student.objects.get(id=pk)
    form = GradeForm(instance=student)
    grades = Grade.objects.filter(foreign_key=pk)
    context = { 'student': student, 'form': form, 'grades': grades }
    
    if request.method == "POST":
        grade = Grade.objects.create(foreign_key=student)
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
        if grade.average == 0.0:
            grade.calculate_average()
            grade.save()
        return redirect('/')
    return render(request, 'app/update_student_grade.html', context)


def update_grade(request, pk):
    student = Student.objects.get(id=pk)
    grade = Grade.objects.get(foreign_key=student)
    form = GradeForm(instance=student)
    context = { 'student': student, 'form': form }

    if request.method == "POST":
        form = GradeForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'app/update_grade.html', context)


def delete_grade(request, pk):
    context = {}
    return render(request, 'app/delete_grade.html', context)


def delete_student(request, pk):
    student = Student.objects.get(id=pk)
    context = { 'student': student }
    
    if request.method == "POST":
        student.delete()
        return redirect('/')
    return render(request, 'app/delete_student.html', context)
