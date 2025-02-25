from .views import home, about_page, subscribe
from django.urls import path
from . import views


urlpatterns = [
    path('', home, name='home'),
    path('about/', about_page, name='about_page'),
    path("subscribe/", subscribe, name="subscribe"),

    path('posts/', views.post_list_view, name='post_list'),
    path('add_post/', views.add_post_view, name='add_post'),
    path('delete/<int:post_id>/', views.delete_post_view, name='delete_post'),
    path('post/edit/<int:post_id>/', views.edit_post_view, name='edit_post'),

]
