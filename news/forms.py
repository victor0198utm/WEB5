from dataclasses import field
from pyexpat import model
from django import forms

from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('password', 'title', 'slug', 'protected', 'private', 'description', 'body', 'image')