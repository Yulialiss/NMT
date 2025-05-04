from django import forms
from .models import Assignment
from .models import AssignmentSubmission
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.forms import modelformset_factory
from django import forms
from django.forms import modelformset_factory
from .models import AssignmentSubmission

class GradeForm(forms.ModelForm):
    class Meta:
        model = AssignmentSubmission
        fields = ['grade']
        labels = {'grade': 'Оцінка'}

GradeFormSet = modelformset_factory(AssignmentSubmission, form=GradeForm, extra=0)

class AssignmentForm(forms.ModelForm):
    instructions = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Assignment
        fields = ['title', 'instructions', 'attachment', 'deadline', 'points']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class AssignmentSubmissionForm(forms.ModelForm):
    class Meta:
        model = AssignmentSubmission
        fields = ['file_submission', 'text_submission']
