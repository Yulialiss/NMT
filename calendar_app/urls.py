from django.urls import path
from .views import calendar_view

app_name = 'calendar_app'

urlpatterns = [
    path('', calendar_view, name='calendar'),
]
