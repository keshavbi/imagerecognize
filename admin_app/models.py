# from django.db import models
from django.shortcuts import render
from django.db import models
# from django.urls import reverse

# from django.core.url import reverse
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image_url = models.TextField(max_length=256)
    # For Image field
    image = models.ImageField(upload_to='images/')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=256)
    length = models.PositiveIntegerField()
    release_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Customer(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone = models.PositiveIntegerField()


class Project(models.Model):
    name = models.CharField(max_length=256)
    manager = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("admin_app:project-detail",kwargs={'pk':self.pk})

class Employee(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    project = models.ForeignKey(Project, related_name='employees', on_delete=models.CASCADE)
    # school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("admin_app:employee-detail",kwargs={'pk':self.pk})
