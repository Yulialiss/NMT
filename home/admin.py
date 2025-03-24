from django.contrib import admin
from .models import Post, Review
from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'preparation_levels', 'price_per_hour', 'created_at', 'subjects')
    search_fields = ('first_name', 'last_name', 'subjects')
    list_filter = ('preparation_levels', 'subjects')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    fields = ('first_name', 'last_name', 'phone_number', 'email', 'preparation_levels', 'subjects', 'price_per_hour', 'photo', 'about', 'calendar', 'created_at')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'content')
    search_fields = ['user__username', 'content']
    list_filter = ('created_at',)

admin.site.register(Post, PostAdmin)
admin.site.register(Review, ReviewAdmin)
