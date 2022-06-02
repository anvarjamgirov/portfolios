from django.db import models

from portfolios.settings import STUDENT


class Student(models.Model):
    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,
    )
    middle_name = models.CharField(
        max_length=255,
    )
    username = models.CharField(
        max_length=127,
        unique=True,
    )
    photo = models.FileField(
        upload_to="uploads/student-photos/",
        null=True,
        blank=True,
    )
    birth_date = models.DateField()
    gender = models.CharField(
        max_length=15,
        choices=STUDENT.GENDER.CHOICES,
    )
    address = models.TextField(
        null=True,
        blank=True,
    )
    passions = models.ManyToManyField(
        'classifiers.Passion',
        related_name='students',
        blank=True,
    )
    position = models.ForeignKey(
        'classifiers.Position',
        on_delete=models.SET_NULL,
        related_name='students',
        null=True,
        blank=True,
    )
    views_count = models.PositiveIntegerField(
        default=0,
    )
    is_active = models.BooleanField(
        default=False,
    )
    added_time = models.DateTimeField(
        auto_now_add=True,
    )
    last_updated_time = models.DateTimeField(
        auto_now=True,
    )

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    def __str__(self):
        return self.full_name


class Education(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='educations',
    )
    university = models.ForeignKey(
        'classifiers.University',
        on_delete=models.CASCADE,
        related_name='educations',
    )
    speciality = models.ForeignKey(
        'classifiers.Speciality',
        on_delete=models.CASCADE,
        related_name='educations',
    )
    start_year = models.PositiveSmallIntegerField()
    graduate_year = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )
    added_time = models.DateTimeField(
        auto_now_add=True,
    )
    last_updated_time = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"{self.student}'s education at {self.university} in {self.speciality}"

    class Meta:
        ordering = ['start_year', ]


class Achievement(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='achievements',
    )
    title = models.CharField(
        max_length=255,
    )
    description = models.TextField()
    date = models.DateField()
    added_time = models.DateTimeField(
        auto_now_add=True,
    )
    last_updated_time = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"{self.student}'s achievement {self.title}"


class Post(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    title = models.CharField(
        max_length=255,
    )
    description = models.TextField()
    body = models.TextField()
    added_time = models.DateTimeField(
        auto_now_add=True,
    )
    last_updated_time = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"{self.student}'s achievement {self.title}"
