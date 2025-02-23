from django import forms
from .models import TeacherProfile

class TeacherProfileForm(forms.ModelForm):
    subjects = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2, 'placeholder': 'Введіть предмети через кому'}),
        required=False,
        label="Предмети викладання"
    )

    class Meta:
        model = TeacherProfile
        fields = ['photo', 'bio', 'subjects', 'phone_number', 'email', 'teaching_mode', 'location', 'age']
