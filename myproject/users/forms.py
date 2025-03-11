from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import User


class CustomUserCreationForm(UserCreationForm):

    usable_password = None

    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('avatar', 'email', 'first_name', 'last_name', 'phone_number', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update({
            'placeholder': 'Введите ваш email',
            'class': "form-control"
        })

        self.fields["first_name"].widget.attrs.update({
            'placeholder': "Укажите ваше имя",
            'class': "form-control"
        })

        self.fields["last_name"].widget.attrs.update({
            'placeholder': "Укажите вашу фамилию",
            'class': "form-control"
        })

        self.fields["phone_number"].widget.attrs.update({
            'placeholder': "Напишите свой номер телефона",
            'class': "form-control"
        })

        self.fields["country"].widget.attrs.update({
            'placeholder': "Укажите страну",
            'class': "form-control"
        })

        self.fields["avatar"].widget.attrs.update({
            'class': "form-control"
        })
