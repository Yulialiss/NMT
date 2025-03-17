from .views import home, about_page, subscribe
from django.urls import path
from . import views
from .views import generate_payment


from .views import rate_post

urlpatterns = [
    path('', home, name='home'),
    path('about/', about_page, name='about_page'),
    path("subscribe/", subscribe, name="subscribe"),

    path('posts/', views.post_list_view, name='post_list'),
    path('add_post/', views.add_post_view, name='add_post'),
    path('delete/<int:post_id>/', views.delete_post_view, name='delete_post'),
    path('post/edit/<int:post_id>/', views.edit_post_view, name='edit_post'),
    path('rate_post/<int:post_id>/', rate_post, name='rate_post'),
    path("pay/", views.pay, name="pay"),
    path("pay/payment.html", views.payment_view, name="payment"),
    path("generate-payment/", generate_payment, name="generate_payment"),

]
