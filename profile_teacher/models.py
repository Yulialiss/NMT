from django.db import models
from django.conf import settings

class TeacherProfile(models.Model):
    TEACHING_MODES = [
        ('online', 'Онлайн'),
        ('offline', 'Очно'),
        ('mixed', 'Змішано'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='teacher_profile')
    bio = models.TextField(blank=True, null=True, verbose_name="Про себе")
    subjects = models.TextField(blank=True, verbose_name="Предмети викладання (перераховуйте через кому)")
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Номер телефону")
    email = models.EmailField(blank=True, verbose_name="Електронна пошта")
    teaching_mode = models.CharField(max_length=10, choices=TEACHING_MODES, default='online', verbose_name="Формат навчання")
    location = models.CharField(max_length=255, blank=True, verbose_name="Локація (місто, область)")
    photo = models.ImageField(upload_to='teacher_photos/', blank=True, null=True, verbose_name="Фото профілю")
    age = models.PositiveIntegerField(blank=True, null=True, verbose_name="Вік")

    def __str__(self):
        return f"Профіль вчителя: {self.user.username}"

    def get_subjects_list(self):
        return [subject.strip() for subject in self.subjects.split(",") if subject.strip()]
