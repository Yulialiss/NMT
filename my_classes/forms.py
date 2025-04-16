from django import forms
from .models import Assignment
from django import forms
from .models import AssignmentSubmission

from django import forms
from .models import Assignment
from ckeditor.widgets import CKEditorWidget

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
