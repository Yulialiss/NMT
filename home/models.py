
from django.db import models
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    first_name = models.CharField(max_length=100, verbose_name="Ім'я")
    last_name = models.CharField(max_length=100, verbose_name="Прізвище")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефону", blank=True, null=True)
    email = models.EmailField(verbose_name="Email", blank=True, null=True)
    preparation_levels = models.CharField(max_length=255, verbose_name="Підготовка до класів")
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Вартість заняття (₴/год)")
    photo = models.ImageField(upload_to='post_photos/', verbose_name="Фото профілю")
    about = models.TextField(blank=True, verbose_name="Про себе")
    calendar = models.TextField(blank=True, verbose_name="Календар")
    created_at = models.DateTimeField(auto_now_add=True)
    subjects = models.CharField(max_length=255, verbose_name="Предмети", default="")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.preparation_levels}"

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.created_at}"
