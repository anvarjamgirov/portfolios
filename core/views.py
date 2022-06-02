from django.shortcuts import render

from students.models import Student


def index(request):
    _ = Student.objects.filter(is_active=True)
    return render(request, 'index.html', {'students': _[:10]})


def students(request):
    _ = Student.objects.filter(is_active=True)
    return render(request, 'students.html', {'students': _})


def student_detail(request, username: str):
    try:
        student = Student.objects.get(username=username)
        return render(request, 'student-detail.html', {'student': student})
    except Student.DoesNotExist:
        return render(request, '404.html')
