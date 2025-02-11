from django.urls import path
from .views import calendar_view, add_event, learning_view
from . import views

urlpatterns = [
    path('', learning_view, name='learning'),
    path('calendar/', calendar_view, name='calendar_view'),
    path('add-event/', add_event, name='add_event'),

]
