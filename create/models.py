from django import forms


class PostForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
