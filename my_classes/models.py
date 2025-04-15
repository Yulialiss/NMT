from django.db import models
from django.conf import settings
import random
import string

class Class(models.Model):
    class_name = models.CharField(max_length=100, default='Default audience')
    section = models.CharField(max_length=100, default='Default audience')
    subject = models.CharField(max_length=100, default='Default audience')
    audience = models.CharField(max_length=255, default='Default audience')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True  # дозволяє створити міграцію, не вимагаючи значення
    )
    password = models.CharField(max_length=8, blank=True, null=True)  # Поле для пароля
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='classes', blank=True)  # Зв'язок з учнями

    def generate_password(self):
        """Метод для генерації пароля з випадкових букв та цифр."""
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        self.password = password
        self.save()

    def __str__(self):
        return self.class_name


class StudentClass(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student.username} в класі {self.class_obj.class_name}'