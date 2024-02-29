from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from config import RenderIfLoggedIn, config


class Login(forms.Form):
    username = forms.CharField(label='Your Ion Username')
    password = forms.CharField(
        widget=forms.PasswordInput()
    )


def make_auth(request):
    if config.authorized:
        return HttpResponseRedirect('/blog')
    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():
            config.authorized = True
            return HttpResponseRedirect('/loggedin')
    else:
        form = Login()
    return render(request, 'auth.html', {"form": Login()})


class LoggedIn(RenderIfLoggedIn):
    main = 'logged_in.html'
