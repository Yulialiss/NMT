from django.contrib import admin
from .models import Post, Review
from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'preparation_levels', 'price_per_hour', 'created_at', 'subjects')  # Вибір полів для відображення в списку
    search_fields = ('first_name', 'last_name', 'subjects')
    list_filter = ('preparation_levels', 'subjects')
    ordering = ('-created_at',)  # Сортування за датою створення (спочатку нові)
    readonly_fields = ('created_at',)  # Поле для перегляду, але не редагування
    fields = ('first_name', 'last_name', 'phone_number', 'email', 'preparation_levels', 'subjects', 'price_per_hour', 'photo', 'about', 'calendar', 'created_at')  # Поля для перегляду та редагування


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'content')
    search_fields = ['user__username', 'content']
    list_filter = ('created_at',)

# Реєстрація моделей
admin.site.register(Post, PostAdmin)
admin.site.register(Review, ReviewAdmin)
