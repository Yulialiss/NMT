from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Розширена модель користувача, якщо потрібно додати додаткові поля"""
    pass
