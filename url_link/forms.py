from .models import ModelUrl
from django import forms


class CreateUrlShort(forms.ModelForm):
    class Meta:
        model = ModelUrl
        fields = ['original_url', 'title', 'short_url']
