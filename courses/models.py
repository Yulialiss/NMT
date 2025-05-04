from django.db import models
from django.conf import settings

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    photo = models.ImageField(upload_to='course_photos/', null=True, blank=True)
    learn_outcome = models.TextField(default='Теми, які будуть розглянуті на курсі.')
    course_format = models.TextField( help_text="Список тем та план курсу", default="Not provided")
    start_date = models.DateField(null=True, blank=True, help_text="Дата початку курсу")
    end_date = models.DateField(null=True, blank=True, help_text="Дата завершення курсу")

    def __str__(self):
        return self.title
