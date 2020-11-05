from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:  # This acts like a config
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
