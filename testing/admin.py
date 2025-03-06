from django.contrib import admin
from .models import Subject, Test, Question, Answer

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
    list_display = ('title', 'subject', 'duration', 'get_test_theme')
    list_editable = ('duration',)
    inlines = [QuestionInline]

    def get_test_theme(self, obj):
        test_count = Test.objects.filter(subject=obj.subject).count()
        return f"Тема {test_count}"
    get_test_theme.short_description = 'Тема'


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'test')
    search_fields = ('text',)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')
    list_filter = ('is_correct',)
    search_fields = ('text',)
