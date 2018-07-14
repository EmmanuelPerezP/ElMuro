from django import forms
from django.core.validators import RegexValidator


class CreatePost(forms.Form):
    image = forms.ImageField(required=False)
    message = forms.CharField(label='Mensaje o shitpost',
                              widget=forms.Textarea(
                                  attrs={'class': 'form-control', 'rows': '3'}))
