from django.urls import path
from .views import teacher_profile_view, teacher_profile_edit

urlpatterns = [
    path('', teacher_profile_view, name='teacher_profile'),
    path('edit/', teacher_profile_edit, name='teacher_profile_edit'),
]
