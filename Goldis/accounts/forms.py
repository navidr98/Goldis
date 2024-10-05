from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserLoginForm(forms.Form):
    username = forms.CharField(label='نام کابری', widget=forms.TextInput(attrs={'class': ''}))
    password = forms.CharField(label='رمز عبور',widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور', 'class': ''}))