from django.urls import path
from .views import subject_list, topic_list, theory_detail

app_name = 'theory'

urlpatterns = [
    path('courses/', subject_list, name='course_list'),
    path('courses/<int:subject_id>/lessons/', topic_list, name='lesson_list'),
    path('lessons/<int:topic_id>/content/', theory_detail, name='lesson_detail'),
]