from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'price', 'photo', 'learn_outcome', 'course_format','start_date',  'end_date']
