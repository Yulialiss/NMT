from django import forms
from .models import Answer

class TestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        test = kwargs.pop('test')
        super().__init__(*args, **kwargs)
        self.test = test
        for question in test.questions.all():
            choices = [(answer.id, answer.text) for answer in question.answers.all()]
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                choices=choices, widget=forms.RadioSelect)
