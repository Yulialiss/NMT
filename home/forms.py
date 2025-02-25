from .models import Review

from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'preparation_levels', 'price_per_hour', 'photo', 'about', 'calendar', 'subjects']
        labels = {
            'first_name': "Ім'я",
            'last_name': "Прізвище",
            'phone_number': "Номер телефону",
            'email': "Email",
            'subjects': "Предмети",
            'preparation_levels': "Підготовка до класів",
            'price_per_hour': "Вартість заняття (₴/год)",
            'about': "Про себе",
            'calendar': "Календар"
        }
        widgets = {
            'subjects': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Наприклад, +380123456789'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your@example.com'}),
            'preparation_levels': forms.TextInput(attrs={'class': 'form-control'}),
            'price_per_hour': forms.NumberInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control'}),
            'calendar': forms.Textarea(attrs={'class': 'form-control'}),
        }


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



