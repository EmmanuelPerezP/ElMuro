from django import forms


class CreatePost(forms.Form):
    image = forms.ImageField(required=False)
    message = forms.CharField(label='Mensaje o shitpost',
                              widget=forms.Textarea(
                                  attrs={'class': 'form-control', 'rows': '3'}))


class CreateComment(forms.Form):
    message = forms.CharField(label='Comentario',
                              widget=forms.Textarea(
                                  attrs={'class': 'form-control', 'rows': '3'}))