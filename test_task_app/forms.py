from django import forms
from .models import *


class LoginPersonForm(forms.Form):

    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Логин', 'class': 'login--input'}))
    password = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Пароль', 'class': 'login--input'}))
