from django import forms
from django.contrib.auth.forms import UsernameField, \
    AuthenticationForm as DjangoAuthenticationForm, UserCreationForm as DjangoUserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, PasswordInput


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
        required=False,
        widget=forms.PasswordInput(
            attrs={
                'class': "form-styling",
                'type': "text",
                'name': "password",
                "placeholder": "Введите свой пароль тут..."
            })
    )


class UserCreationForm(DjangoUserCreationForm):
    password1 = forms.CharField(label='', required=True, strip=False, widget=PasswordInput(attrs={
        "class": "form-styling",
        "type": "text",
        "name": "password",
        "placeholder": ""

    }))
    password2 = forms.CharField(label='', required=False, strip=False, widget=PasswordInput(attrs={
        "class": "form-styling",
        "type": "text",
        "name": "confirmpassword",
        "placeholder": ""
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': TextInput(attrs={
                "class": "form-styling",
                "type": "text",
                "name": "fullname",
                "placeholder": ""
            }),
            'email': EmailInput(attrs={
                "class": "form-styling",
                "type": "text",
                "name": "email",
                "placeholder": ""
            })
        }
