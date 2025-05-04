from django.contrib import admin
from .models import Class, Assignment, StudentClass, AssignmentSubmission

class ClassAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'section', 'subject', 'audience', 'author', 'teacher_first_name', 'teacher_last_name', 'password')
    search_fields = ('class_name', 'section', 'subject')
    filter_horizontal = ('students',)

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'school_class', 'deadline', 'points', 'created_at')
    search_fields = ('title', 'author__username', 'school_class__class_name')
    list_filter = ('school_class', 'created_at')

class StudentClassAdmin(admin.ModelAdmin):
    list_display = ('student', 'class_obj')
    search_fields = ('student__username', 'class_obj__class_name')

class AssignmentSubmissionAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'student', 'file_submission', 'submitted_at', 'grade')
    search_fields = ('assignment__title', 'student__username')
    list_filter = ('grade',)

admin.site.register(Class, ClassAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(StudentClass, StudentClassAdmin)
admin.site.register(AssignmentSubmission, AssignmentSubmissionAdmin)
