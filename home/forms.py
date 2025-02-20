from .models import Review
from django import forms

class SubscribeForm(forms.Form):
    email = forms.EmailField(label="Ваш Email", widget=forms.EmailInput(attrs={"class": "form-control"}))


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Напишіть ваш відгук тут', 'rows': 4, 'cols': 40}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label = False



