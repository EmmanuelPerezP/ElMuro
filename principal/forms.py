from django import forms
from django.core.exceptions import ValidationError


class CreatePost(forms.Form):
    image = forms.ImageField(label='Imagen (opcional)', required=False)
    message = forms.CharField(label='Mensaje o shitpost',
                              widget=forms.Textarea(
                                  attrs={'class': 'form-control', 'rows': '3'}))

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 5*1024*1024:
                raise ValidationError("Imagen muy grande tiene que ser menor a 5mb ")
            return image


class CreateComment(forms.Form):
    message = forms.CharField(label='Comentario',
                              widget=forms.Textarea(
                                  attrs={'class': 'form-control', 'rows': '3'}))
