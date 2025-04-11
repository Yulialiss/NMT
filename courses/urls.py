from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses_page, name='courses'),
    path('add/', views.add_course, name='add_course'),
    path('course/<int:id>/', views.course_detail, name='course_detail'),
    path('course/<int:id>/edit/', views.edit_course, name='edit_course'),

]
