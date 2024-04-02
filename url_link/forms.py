from .models import SaveUrlShortened
from django import forms


class CreateUrlShort(forms.ModelForm):
    class Meta:
        model = SaveUrlShortened
        fields = ['original_url', 'title', 'short_url']
