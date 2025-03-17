from django.db import models
from django.contrib.auth import get_user_model
from datetime import timedelta

CustomUser = get_user_model()

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Test(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='tests')
    title = models.CharField(max_length=200)
    duration = models.IntegerField(help_text="Тривалість у хвилинах", default=60)

    def __str__(self):
        return self.title

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()

    def __str__(self):
        return self.text[:50]

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class TestResult(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField()
    max_score = models.IntegerField(default=0)
    date_taken = models.DateTimeField(auto_now_add=True)
    time_spent = models.DurationField(default=timedelta())

    def formatted_time_spent(self):
        minutes, seconds = divmod(int(self.time_spent.total_seconds()), 60)
        return f"{minutes} хв {seconds} сек"

    def __str__(self):
        return f"{self.user.username} - {self.test.title} - {self.score}/{self.max_score} балів - {self.formatted_time_spent()}"

class IncorrectAnswer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.test.title} - Неправильна відповідь на {self.question.text}"
