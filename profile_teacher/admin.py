
from django.contrib import admin
from .models import TeacherProfile

@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'phone_number', 'teaching_mode', 'location', 'age')
    search_fields = ('user__username', 'email', 'phone_number', 'subjects', 'location')
    list_filter = ('teaching_mode', 'age')

    fieldsets = (
        (None, {'fields': ('user', 'photo')}),
        ('Контактна інформація', {'fields': ('email', 'phone_number', 'location')}),
        ('Професійна інформація', {'fields': ('subjects', 'teaching_mode', 'bio', 'age')}),
    )

admin.site.site_header = "Адміністрування платформи"
admin.site.site_title = "Адмінка"
admin.site.index_title = "Керування даними"
