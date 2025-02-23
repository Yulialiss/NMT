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
        self.fields['first_name'].widget.attrs['placeholder'] = "Ім'я"
        self.fields['last_name'].widget.attrs['placeholder'] = 'Прізвище'
        self.fields['email'].widget.attrs['placeholder'] = 'email@example.com'

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birth_date', 'photo', 'bio', 'phone_number', 'location']
        widgets = {
            'photo': CustomClearableFileInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['birth_date'].widget.attrs['placeholder'] = 'ДД/MM/РРРР'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Ваш номер телефону'
        self.fields['location'].widget.attrs['placeholder'] = 'Місто/Регіон'
