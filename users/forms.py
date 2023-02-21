from django import forms
from django.contrib.auth.forms import UsernameField, \
    AuthenticationForm as DjangoAuthenticationForm, UserCreationForm as DjangoUserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput


class AuthorizationForm(DjangoAuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': "form-styling",
            'type': "text",
            'name': "username",
            "placeholder": "Введите свой логин тут..."
        }
    ))
    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': "form-styling",
                'type': "text",
                'name': "password",
                "placeholder": "Введите свой пароль тут..."
            })
    )


class UserCreationForm(DjangoUserCreationForm):
    email = forms.EmailField(max_length=254, help_text='This field is required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
        widgets = {
            'first_name': TextInput(attrs={
                'type': 'text',
                'name': 'first-name-add',
                'id': 'first-name-add',
                'placeholder': '',
                'class': 'bg-gray-200 border border-gray-300 text-gray-900 text-sm rounded-r-lg w-full p-2.5'
            }),
            'last_name': TextInput(attrs={
                'type': 'text',
                'name': 'last-name-add',
                'id': 'last-name-add',
                'placeholder': '',
                'class': 'bg-gray-200 border border-gray-300 text-gray-900 text-sm rounded-r-lg w-full p-2.5'
            }),

            'patronymic': TextInput(attrs={
                'type': 'text',
                'name': 'patronymic-add',
                'id': 'patronymic-add',
                'placeholder': '',
                'class': 'bg-gray-200 border border-gray-300 text-gray-900 text-sm rounded-r-lg w-full p-2.5'
            }),
            'position': TextInput(attrs={
                'type': 'text',
                'name': 'position-add',
                'id': 'position-add',
                'placeholder': '',
                'class': 'bg-gray-200 border border-gray-300 text-gray-900 text-sm rounded-r-lg w-full p-2.5'
            }),
        }