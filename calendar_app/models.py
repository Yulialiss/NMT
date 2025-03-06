from django.db import models
from django.conf import settings

class Event(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return self.title
