from django.urls import path

from .views import index, students, student_detail, post_detail

urlpatterns = [
    path('', index),
    path('students/', students),
    path('students/<str:username>/', student_detail),
    path('posts/<int:post_id>/', post_detail)
]
