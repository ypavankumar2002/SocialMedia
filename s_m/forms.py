from .models import Media
from django import forms


class Mediaform(forms.ModelForm):

    class Meta:
        model = Media
        fields = ['title', 'image', 'video', 'user']





