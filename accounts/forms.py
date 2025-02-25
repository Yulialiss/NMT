from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    pass

class RegisterForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=CustomUser.ROLE_CHOICES,
        widget=forms.RadioSelect,
        label="Оберіть роль"
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'password1', 'password2']
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }
        error_messages = {
            'password1': {
                'too_common': 'Пароль не може бути занадто простим.',
                'too_similar': 'Пароль не може бути схожим на ваше інше особисте інформацію.',
                'too_short': 'Пароль повинен містити не менше 8 символів.',
                'numeric': 'Пароль не може бути повністю числовим.',
            },
        }
