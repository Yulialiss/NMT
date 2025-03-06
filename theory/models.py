from django.db import models
from ckeditor.fields import RichTextField

class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Theory(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = RichTextField()

    def __str__(self):
        return f"Теорія для {self.topic.name}"
