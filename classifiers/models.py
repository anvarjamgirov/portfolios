from django.db import models


class University(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
    )
    added_time = models.DateTimeField(
        auto_now_add=True,
    )
    last_updated_time = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name


class Speciality(models.Model):
    name = models.CharField(
        max_length=511,
        unique=True,
    )
    added_time = models.DateTimeField(
        auto_now_add=True,
    )
    last_updated_time = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name


class Passion(models.Model):
    name = models.CharField(
        max_length=127,
        unique=True,
    )
    added_time = models.DateTimeField(
        auto_now_add=True,
    )
    last_updated_time = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(
        max_length=127,
        unique=True,
    )
    added_time = models.DateTimeField(
        auto_now_add=True,
    )
    last_updated_time = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name
