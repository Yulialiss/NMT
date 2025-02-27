from django.db import models
from django.conf import settings
from django.db.models import Avg


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

    rating = models.FloatField(default=0.0, verbose_name="Середній рейтинг")
    rating_count = models.IntegerField(default=0, verbose_name="Кількість оцінок")

    def update_rating(self):
        avg_rating = self.ratings.aggregate(Avg('score'))['score__avg']
        self.rating = avg_rating if avg_rating else 0
        self.rating_count = self.ratings.count()
        self.save()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.preparation_levels}"

class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="ratings")
    score = models.IntegerField(verbose_name="Оцінка")

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} - {self.score}"

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.created_at}"
