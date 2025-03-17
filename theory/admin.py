from django.contrib import admin
from .models import Subject, Topic, Theory
from ckeditor.widgets import CKEditorWidget
from django.db import models

class TheoryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }
    list_display = ('topic', 'video_url')

admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(Theory, TheoryAdmin)
