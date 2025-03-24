from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import ClearableFileInput
from .models import Profile

class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = ''
    initial_text = ''
    input_text = 'Вибрати фото'
    template_name = 'widgets/custom_clearable_file_input.html'

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'placeholder': "Ім'я",
            'class': 'form-control rounded-pill'
        })
        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Прізвище',
            'class': 'form-control rounded-pill'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'email@example.com',
            'class': 'form-control rounded-pill'
        })

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birth_date', 'photo', 'bio', 'phone_number', 'location']
        widgets = {
            'photo': CustomClearableFileInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['birth_date'].widget.attrs.update({
            'placeholder': 'дд.мм.рррр',
            'class': 'form-control rounded-pill'
        })
        self.fields['birth_date'].input_formats = ['%d.%m.%Y']

        self.fields['phone_number'].widget.attrs.update({
            'placeholder': 'Ваш номер телефону',
            'class': 'form-control rounded-pill'
        })
        self.fields['location'].widget.attrs.update({
            'placeholder': 'Місто/Регіон',
            'class': 'form-control rounded-pill'
        })

        self.fields['photo'].required = False
