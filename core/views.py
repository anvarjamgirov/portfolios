from django.db.models import Q
from django.shortcuts import render

from students.models import Student, Post


def index(request):
    _ = Student.objects.filter(is_active=True)
    return render(request, 'index.html', {'students': _[:10]})


def students(request):
    q = request.GET.get('q', None)
    _ = Student.objects.filter(is_active=True)
    if q:
        _ = _.filter(
            Q(first_name__icontains=q) | Q(last_name__icontains=q) | Q(middle_name__icontains=q)
        )
    return render(request, 'students.html', {'students': _})


def student_detail(request, username: str):
    try:
        student = Student.objects.get(username=username)
        student.views_count += 1
        student.save()
        return render(request, 'student-detail.html', {'student': student})
    except Student.DoesNotExist:
        return render(request, '404.html')


def post_detail(request, post_id: int):
    try:
        post = Post.objects.get(id=post_id)
        return render(request, 'post-detail.html', {'post': post})
    except Post.DoesNotExist:
        return render(request, '404.html')
