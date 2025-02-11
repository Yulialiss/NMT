from django.urls import path
from .views import home, about_page, subscribe

urlpatterns = [
    path('', home, name='home'),
    path('about/', about_page, name='about_page'),
    path("subscribe/", subscribe, name="subscribe"),
]
