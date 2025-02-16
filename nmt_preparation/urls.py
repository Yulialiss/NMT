from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('profile/', include('profile_app.urls')),
    path('learning/', include('learning.urls')),
    path('contact/', include('contact.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('testing/', include('testing.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
