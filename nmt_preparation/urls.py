from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('profile/', include('profile_app.urls')),
    path('contact/', include('contact.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('testing/', include('testing.urls')),
    path('teacher/', include('profile_teacher.urls')),
    path('calendar/', include('calendar_app.urls')),
    path('theory/', include('theory.urls')),
    path('courses/', include('courses.urls')),
                  path('my_classes/', include('my_classes.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
