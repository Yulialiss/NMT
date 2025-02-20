from django.urls import path
from . import views
from .views import time_up

urlpatterns = [
    path('testing/', views.subject_list, name='subject_list'),
    path('testing/<int:subject_id>/', views.test_list, name='test_list'),
    path('testing/test/<int:test_id>/', views.test_detail, name='test_detail'),
    path('testing/result/<int:result_id>/', views.test_result, name='test_result'),
    path('time_up/<int:test_id>/', time_up, name='time_up'),

]
