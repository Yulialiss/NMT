from django.db import models
from django.conf import settings
import random
import string
from django.db import models

from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField


class Class(models.Model):
    class_name = models.CharField(max_length=100, default='Default audience')
    section = models.CharField(max_length=100, default='Default audience')
    subject = models.CharField(max_length=100, default='Default audience')
    audience = models.CharField(max_length=255, default='Default audience')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True)
    password = models.CharField(max_length=8, blank=True, null=True)
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='classes', blank=True)
    teacher_first_name = models.CharField(max_length=100, blank=True, null=True)
    teacher_last_name = models.CharField(max_length=100, blank=True, null=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True  
    )
    password = models.CharField(max_length=8, blank=True, null=True) 
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='classes', blank=True)  


    def generate_password(self):
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        self.password = password
        self.save()

    def __str__(self):
        return self.class_name

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    instructions = RichTextField(blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    school_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='assignments')
    attachment = models.FileField(upload_to='assignments_files/', blank=True, null=True)
    deadline = models.DateTimeField(null=True, blank=True)
    points = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class StudentClass(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student.username} в класі {self.class_obj.class_name}'


class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file_submission = models.FileField(upload_to='submissions/', blank=True, null=True)
    text_submission = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    grade = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.student.username} submitted for {self.assignment.title}'
