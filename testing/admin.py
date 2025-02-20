from django.contrib import admin
from .models import Subject, Test, Question, Answer, Event

admin.site.register(Subject)

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    inlines = [AnswerInline]

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'duration')
    list_editable = ('duration',)
    inlines = [QuestionInline]

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    list_filter = ('date',)
    search_fields = ('title', 'description', 'location')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'test')
    search_fields = ('text',)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')
    list_filter = ('is_correct',)
    search_fields = ('text',)
