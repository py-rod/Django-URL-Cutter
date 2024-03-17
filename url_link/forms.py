from .models import SaveUrlShortened
from django.contrib.auth import get_user_model
from django import forms


class CreateUrlShort(forms.ModelForm):
    class Meta:
        model = SaveUrlShortened
        fields = ['original_url', 'title', 'short_url']
