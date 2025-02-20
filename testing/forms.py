from django import forms
from .models import Event, Test, Answer

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location']


class TestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        test = kwargs.pop('test')
        super().__init__(*args, **kwargs)
        self.test = test

        for question in test.questions.all():
            choices = [(answer.id, answer.text) for answer in question.answers.all()]
            if choices:
                self.fields[f'question_{question.id}'] = forms.ChoiceField(
                    choices=choices,
                    widget=forms.RadioSelect,
                    label=question.text
                )

    def clean(self):
        cleaned_data = super().clean()

        for question in self.test.questions.all():
            if f'question_{question.id}' not in cleaned_data:
                raise forms.ValidationError(f"Відповідь на питання '{question.text}' не може бути порожньою.")

        return cleaned_data
