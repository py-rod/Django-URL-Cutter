from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django_recaptcha.fields import ReCaptchaField, ReCaptchaV3


class UserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email", "password1", "password2"]

    def save(self, commit=True) -> Any:
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class AuthenticationForm(AuthenticationForm):
    def __init__(self,  *args, **kwargs) -> None:
        super(AuthenticationForm, self).__init__(*args, **kwargs)

    username = forms.EmailInput(
        attrs={"type": "email", "autocomplete":  True, "autofocus": True})

    captcha = ReCaptchaField(widget=ReCaptchaV3(attrs={
        'required_score': 0.80,
        'size': 'compact',
        'theme': 'dark',
        'action': 'signin'
    }))
