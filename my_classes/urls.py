from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_classes, name='my_classes'),
    path('create_class/', views.create_class, name='create_class'),
    path('class/<int:class_id>/', views.class_detail, name='class_detail'),
    path('join-class/', views.join_class, name='join_class'),
    path('class/delete/<int:class_id>/', views.delete_class, name='delete_class'),
    path('class/<int:class_id>/assignments/', views.assignment_list, name='assignment_list'),
    path('class/<int:class_id>/assignments/add/', views.add_assignment, name='add_assignment'),

    path('assignment/<int:assignment_id>/', views.view_assignment, name='view_assignment'),
    path('class/<int:class_id>/members/', views.class_members, name='class_members'),

    path('assignment/<int:assignment_id>/grade/', views.grade_submissions, name='grade_submissions'),
path('submission/<int:submission_id>/delete/', views.delete_submission, name='delete_submission'),

]
