from django import forms
from django.contrib.auth.models import User
from .models import Profile

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['birth_date'].widget.attrs['placeholder'] = 'ДД/MM/РРРР'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Ваш номер телефону'
        self.fields['location'].widget.attrs['placeholder'] = 'Місто/Регіон'
