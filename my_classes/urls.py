from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_classes, name='my_classes'),
    path('create_class/', views.create_class, name='create_class'),
    path('class/<int:class_id>/', views.class_detail, name='class_detail'),
    path('join-class/', views.join_class, name='join_class'),

]
